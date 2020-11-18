from build_graph import set_position_election, get_count_position, show_plot
from get_votes import *

### PRESIDENT ###
# year = 2018
# regional_aggregation = 'Brazil'
# votes_list = get_president_votes_list(year, regional_aggregation)
# print('VOTES LIST')
# for i in votes_list:
#     print(i)


### MAYOR ###
# year = 2016
# uf = 'RN'
# city = 'NATAL'
# code = get_tse_code(uf, city)
# print('CITY CODE')
# votes_list = get_mayor_votes_list(year, code)
# print('VOTES LIST')
# for i in votes_list:
#     print(i)


### GOVERNOR ###
year = 2018
uf = 'SP'
votes_list = get_governor_votes_list(year, uf)
print('VOTES LIST')
for i in votes_list:
    print(i)

votes_list_position = set_position_election(votes_list)
print('VOTES POSITION')
count = get_count_position(votes_list_position)
print('COUNT POSITION')
show_plot(count)