from build_graph import set_position_election, get_count_position, show_plot
from get_votes import *

### PRESIDENT ###
# year = 2018
# regional_aggregation = 'Brazil'
# votes_list = get_president_votes_list(year, regional_aggregation)


### MAYOR ###
year = 2016
uf = 'TO'
city = 'PARAÍSO DO TOCANTINS'
code = get_tse_code(uf, city)
votes_list = get_mayor_votes_list(year, code)


votes_list_position = set_position_election(votes_list)
count = get_count_position(votes_list_position)
show_plot(count)