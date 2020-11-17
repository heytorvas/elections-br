from electionsBR import *

'''
# COALITIONS

['ANO_ELEICAO', 'CODIGO_CARGO', 'COMPOSICAO_COLIGACAO', 'DATA_GERACAO',
'DESCRICAO_CARGO', 'DESCRICAO_ELEICAO', 'HORA_GERACAO',
'NOME_COLIGACAO', 'NOME_PARTIDO', 'NUMERO_PARTIDO', 'NUM_TURNO',
'SEQUENCIA_COLIGACAO', 'SIGLA_COLIGACAO', 'SIGLA_PARTIDO', 'SIGLA_UE',
'SIGLA_UF', 'TIPO_LEGENDA']

# VOTES

['ANO_ELEICAO', 'COD_MUN_TSE', 'COD_MUN_IBGE', 'NOME_MUNICIPIO',
'CODIGO_MICRO', 'NOME_MICRO', 'CODIGO_MESO', 'NOME_MESO', 'UF',
'NOME_UF', 'CODIGO_MACRO', 'NOME_MACRO', 'SIGLA_UE', 'NUM_TURNO',
'DESCRICAO_ELEICAO', 'CODIGO_CARGO', 'DESCRICAO_CARGO',
'NUMERO_CANDIDATO', 'QTDE_VOTOS']

# ELECTIONS
['ANO_ELEICAO', 'NUM_TURNO', 'COD_MUN_TSE', 'COD_MUN_IBGE',
'NOME_MUNICIPIO', 'CODIGO_MICRO', 'NOME_MICRO', 'CODIGO_MESO',
'NOME_MESO', 'UF', 'NOME_UF', 'CODIGO_MACRO', 'NOME_MACRO',
'DESCRICAO_ELEICAO', 'CODIGO_CARGO', 'DESCRICAO_CARGO',
'SIGLA_COLIGACAO', 'NOME_COLIGACAO', 'COMPOSICAO_COLIGACAO',
'QTDE_VOTOS']

'''

# vot = get_votes(year=2018,
#                 position="President", 
#                 regional_aggregation="State", 
#                 candidate_number=17,
#                 filters={"NUM_TURNO": 1},
#                 columns=["NUMERO_CANDIDATO", "UF", "NUM_TURNO", "QTDE_VOTOS"])

# vot = get_votes(year=2016,
#                 position="Mayor",
#                 filters={"COD_MUN_TSE": 73008},
#                 uf="TO")

# leg = get_coalitions(year=2016, position="Mayor",
#                     filters={"SIGLA_UE": "95192"},
#                     columns=["COMPOSICAO_COLIGACAO", "SIGLA_UE"])

def split_party(coalition):
    if '/' in coalition:
        party_list = coalition.split('/')
        for party in range(len(party_list)):
            party_list[party] = party_list[party].strip().replace(' ', '')

        return party_list
    else:
        return coalition

vot = get_elections(
    year=2018, 
    position="President",
    regional_aggregation="Brazil", 
    filters={"NUM_TURNO": 1},
    political_aggregation="Coalition",
    columns=["ANO_ELEICAO", "COMPOSICAO_COLIGACAO", "QTDE_VOTOS"])

votes_list = []

for index, row in vot.iterrows():
    votes = {
        'year_election': row["ANO_ELEICAO"],
        'coalition': split_party(row["COMPOSICAO_COLIGACAO"]),
        'num_votes': row['QTDE_VOTOS']
    }
    votes_list.append(votes)

# print(vot[["COMPOSICAO_COLIGACAO", "QTDE_VOTOS"]])
# print(vot[["ANO_ELEICAO", "COMPOSICAO_COLIGACAO", "QTDE_VOTOS"]])
print(votes_list)

# BRAZIL BY ELECTION - PRESIDENT
# ELECTION IN CITY USING COALITION ???