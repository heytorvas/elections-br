from get_votes import *

uf = 'RJ'
city = 'RIO DE JANEIRO'
year = '2016'

code = get_tse_code(uf, city)

# vot = get_votes(year=2018,
#                 position="President", 
#                 regional_aggregation="State", 
#                 candidate_number=17,
#                 filters={"NUM_TURNO": 1},
#                 columns=["NUMERO_CANDIDATO", "UF", "NUM_TURNO", "QTDE_VOTOS"])


#print(get_candidates_abbrev(year, 'Mayor', code))
#print(job_year_region(year, 'Mayor', 'Municipality', code))
# print(mayor_year_city(year, code))
