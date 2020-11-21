from electionsBR import *
from build_graph import *
import pandas as pd
from util import get_file_json

'''

# GET_COALITIONS
['ANO_ELEICAO', 'CODIGO_CARGO', 'COMPOSICAO_COLIGACAO', 'DATA_GERACAO',
'DESCRICAO_CARGO', 'DESCRICAO_ELEICAO', 'HORA_GERACAO',
'NOME_COLIGACAO', 'NOME_PARTIDO', 'NUMERO_PARTIDO', 'NUM_TURNO',
'SEQUENCIA_COLIGACAO', 'SIGLA_COLIGACAO', 'SIGLA_PARTIDO', 'SIGLA_UE',
'SIGLA_UF', 'TIPO_LEGENDA']

# GET_VOTES
['ANO_ELEICAO', 'COD_MUN_TSE', 'COD_MUN_IBGE', 'NOME_MUNICIPIO',
'CODIGO_MICRO', 'NOME_MICRO', 'CODIGO_MESO', 'NOME_MESO', 'UF',
'NOME_UF', 'CODIGO_MACRO', 'NOME_MACRO', 'SIGLA_UE', 'NUM_TURNO',
'DESCRICAO_ELEICAO', 'CODIGO_CARGO', 'DESCRICAO_CARGO',
'NUMERO_CANDIDATO', 'QTDE_VOTOS']

# GET_ELECTIONS
['ANO_ELEICAO', 'NUM_TURNO', 'COD_MUN_TSE', 'COD_MUN_IBGE',
'NOME_MUNICIPIO', 'CODIGO_MICRO', 'NOME_MICRO', 'CODIGO_MESO',
'NOME_MESO', 'UF', 'NOME_UF', 'CODIGO_MACRO', 'NOME_MACRO',
'DESCRICAO_ELEICAO', 'CODIGO_CARGO', 'DESCRICAO_CARGO',
'SIGLA_COLIGACAO', 'NOME_COLIGACAO', 'COMPOSICAO_COLIGACAO',
'QTDE_VOTOS']

# GET_CANDIDATES
['ANO_ELEICAO', 'NUM_TURNO', 'DESCRICAO_ELEICAO', 'SIGLA_UF', 'SIGLA_UE',
'DESCRICAO_UE', 'CODIGO_CARGO', 'DESCRICAO_CARGO', 'NOME_CANDIDATO',
'SEQUENCIAL_CANDIDATO', 'NUMERO_CANDIDATO', 'CPF_CANDIDATO',
'NOME_URNA_CANDIDATO', 'COD_SITUACAO_CANDIDATURA',
'DES_SITUACAO_CANDIDATURA', 'NUMERO_PARTIDO', 'SIGLA_PARTIDO',
'NOME_PARTIDO', 'CODIGO_LEGENDA', 'SIGLA_LEGENDA', 'COMPOSICAO_LEGENDA',
'NOME_COLIGACAO', 'CODIGO_OCUPACAO', 'DESCRICAO_OCUPACAO',
'DATA_NASCIMENTO', 'NUM_TITULO_ELEITORAL_CANDIDATO',
'IDADE_DATA_ELEICAO', 'CODIGO_SEXO', 'DESCRICAO_SEXO',
'COD_GRAU_INSTRUCAO', 'DESCRICAO_GRAU_INSTRUCAO', 'CODIGO_ESTADO_CIVIL',
'DESCRICAO_ESTADO_CIVIL', 'CODIGO_COR_RACA', 'DESCRICAO_COR_RACA',
'CODIGO_NACIONALIDADE', 'DESCRICAO_NACIONALIDADE',
'SIGLA_UF_NASCIMENTO', 'CODIGO_MUNICIPIO_NASCIMENTO',
'NOME_MUNICIPIO_NASCIMENTO', 'DESPESA_MAX_CAMPANHA',
'COD_SIT_TOT_TURNO', 'DESC_SIT_TOT_TURNO', 'EMAIL_CANDIDATO']

'''


def get_tse_code(uf, name_city):
    tse_codes = get_file_json('assets/tse-code-city.json')
    
    for city in tse_codes:
        if city['uf'] == uf and city['nome_municipio'] == name_city:
            return city['codigo_tse']

def split_party(coalition):
    if isinstance(coalition, float):
        pass

    else:
        if '/' in coalition:
            party_list = coalition.split('/')
            for party in range(len(party_list)):
                party_list[party] = party_list[party].strip().replace(' ', '')

            return party_list
        else:
            party_list = []
            party_list.append(coalition)
            return party_list

def get_votes_president(year, regional_aggregation):
    vot = get_elections(
        year= year, 
        position= 'President',
        regional_aggregation= regional_aggregation, 
        filters={"NUM_TURNO": 1},
        political_aggregation="Coalition",
        columns=["ANO_ELEICAO", "COMPOSICAO_COLIGACAO", "QTDE_VOTOS"])
    
    return vot

def get_president_votes_list(year, regional_aggregation):
    vot = get_votes_president(year, regional_aggregation)
    votes_list = []
    for index, row in vot.iterrows():
        votes = {
            'year_election': row["ANO_ELEICAO"],
            'coalition': split_party(row["COMPOSICAO_COLIGACAO"]),
            'num_votes': row['QTDE_VOTOS']
        }
        votes_list.append(votes)
    
    return votes_list

def get_votes_mayor(year, code):
    vot = get_votes(year=year,
        position="Mayor",
        filters={"COD_MUN_TSE": code},
        columns=["ANO_ELEICAO", "COD_MUN_TSE", "COD_MUN_IBGE",
                "NOME_MUNICIPIO", "NUMERO_CANDIDATO", "QTDE_VOTOS"]
    )
    return vot

def get_candidates_mayor(year, label_ue = ''):
    vot = get_candidates(
        year=year, 
        position="Mayor",
        filters={"NUM_TURNO": 1, "SIGLA_UE": label_ue},
        columns=["ANO_ELEICAO", "NOME_URNA_CANDIDATO", "SIGLA_UE", "NUMERO_PARTIDO", "SIGLA_PARTIDO", "COMPOSICAO_LEGENDA"])

    return vot

def get_mayor_votes_list(year, code):
    votes_mayor = get_votes_mayor(year, code)
    candidates_mayor = get_candidates_mayor(year, code)

    return politics_votes_list(votes_mayor, candidates_mayor)

def get_votes_governor(year, uf):
    vot = get_votes(year=year,
            position="Governor",
            filters={"UF": uf, "NUM_TURNO": 1},
            columns=["ANO_ELEICAO", "UF", "NUM_TURNO", "NUMERO_CANDIDATO", "QTDE_VOTOS"]
    )
    return vot

def get_candidates_governor(year, uf):
    vot = get_candidates(year=year, position="Governor",
                        filters={"SIGLA_UF": uf, "NUM_TURNO": 1},
                        columns=["ANO_ELEICAO", "NUM_TURNO", "SIGLA_UF", "NOME_URNA_CANDIDATO", "NUMERO_PARTIDO", "SIGLA_PARTIDO", "COMPOSICAO_LEGENDA"])
    return vot

def get_governor_votes_list(year, uf):
    votes_governor = get_votes_governor(year, uf)
    candidates_governor = get_candidates_governor(year, uf)

    return politics_votes_list(votes_governor, candidates_governor)

def politics_votes_list(votes, candidates):
    votes_list = []
    for index, row in votes.iterrows():
        for i, r in candidates.iterrows():
            if r["NUMERO_PARTIDO"] == row["NUMERO_CANDIDATO"]:
                votes = {
                    'year_election': row["ANO_ELEICAO"],
                    'city_code': row["COD_MUN_IBGE"],
                    'city': row["NOME_MUNICIPIO"],
                    'name': r["NOME_URNA_CANDIDATO"],
                    'party': r["SIGLA_PARTIDO"],
                    'coalition': split_party(r["COMPOSICAO_LEGENDA"]),
                    'num_votes': row['QTDE_VOTOS']
                }
                votes_list.append(votes)

    return votes_list

def get_votes_president_uf(year, uf):
    vot = get_elections(
            year= year, 
            position= 'President',
            regional_aggregation= 'State', 
            filters={"NUM_TURNO": 1, "UF": uf},
            political_aggregation="Candidate",
            columns=["ANO_ELEICAO", "NUM_TURNO", "COMPOSICAO_COLIGACAO", "QTDE_VOTOS", "UF"])
    return vot

def get_votes_president_list(vot):
    votes_list = []
    for index, row in vot.iterrows():
        coalition = split_party(row["COMPOSICAO_COLIGACAO"])
        votes = {
            'year_election': row["ANO_ELEICAO"],
            'coalition': coalition,
            'num_votes': row['QTDE_VOTOS'],
            'party': coalition[0]
        }
        votes_list.append(votes)
    
    return votes_list

def set_dataframe_president(year):
    states = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",	
 	"MG", "PA", "PB", "PR", "PE", "PI",	"RJ", "RN",	"RS", "RO",	"RR", "SC",	
 	"SP", "SE", "TO"]

    states_list = []
    position_list = []
    count_list = []

    for i in states:
        vot = get_votes_president_uf(year, i)
        votes_list = get_votes_president_list(vot)
        x = set_position_election(votes_list)

        count = get_count_position(x)
        print(count)
        max_key = max(count, key=count.get)
        print(max_key, count[max_key])

        states_list.append(i)
        position_list.append(max_key)
        count_list.append(count[max_key])

    states_json = { 
        'State': states_list, 
        'Position': position_list, 
        'Count': count_list, 
    } 
     
    df = pd.DataFrame(states_json)
    df.to_csv('data/df_president_state_{}.csv'.format(year))

def set_state_cities(uf):
    tse_codes = get_file_json('assets/tse-code-city.json')
    dict_state = []
    for city in tse_codes:
        if city['uf'] == uf:
            dict_city = {
                'name': city['nome_municipio'],
                'uf': city['uf'],
                'tse_code': city['codigo_tse'],
                'ibge_code': city['codigo_ibge']
            }
            dict_state.append(dict_city)
    
    return dict_state

def set_position_from_cities(dict_state, year):
    list_city = []
    #for city in range(326, len(dict_state)):
    for city in dict_state:
        votes_list = get_mayor_votes_list(year, city['tse_code'])
        #votes_list = get_mayor_votes_list(year, dict_state[city]['tse_code'])

        votes_count = []
        for i in votes_list:
            votes_count.append(int(i['num_votes']))
        
        major_vote = largest_votes(votes_count)

        most_votes_candidate = {}
        for i in votes_list:
            if int(i['num_votes']) == major_vote:
                most_votes_candidate = i

        votes_list_position = set_position_election_only(most_votes_candidate)
        list_city.append(votes_list_position)

        print(votes_list_position)
    
    return list_city

def set_dataframe_mayor_state(uf, year):
    dict_state = set_state_cities(uf)
    list_city = set_position_from_cities(dict_state, year)

    year_election = []
    city_code = []
    city = []
    num_votes = []
    position = []

    for i in list_city:
        year_election.append(i['year_election'])
        city_code.append(i['city_code'])
        city.append(i['city'])
        num_votes.append(i['num_votes'])
        position.append(i['position'])

    cities_json = { 
        'Year Election': year_election,
        'City Code': city_code,
        'City': city,
        'Num Votes': num_votes, 
        'Position': position, 
    } 
        
    df = pd.DataFrame(cities_json)
    df.to_csv('data/df_mayor_{}_{}.csv'.format(uf, year), index = False)
    print(df)