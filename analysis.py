from build_graph import *
from get_votes import *

### PRESIDENT ###
def analysis_president(year, regional_aggregation):
    votes_list = get_president_votes_list(year, regional_aggregation)
    print('VOTES LIST')
    for i in votes_list:
        print(i)

    analysis_votes(votes_list)

### MAYOR ###
def analysis_mayor(year, uf, city):
    code = get_tse_code(uf, city)
    print('CITY CODE')
    votes_list = get_mayor_votes_list(year, code)
    print('VOTES LIST')
    for i in votes_list:
        print(i)

    analysis_votes(votes_list)

### GOVERNOR ###
def analysis_governor(year, uf):
    votes_list = get_governor_votes_list(year, uf)
    print('VOTES LIST')
    for i in votes_list:
        print(i)
    
    analysis_votes(votes_list)

def analysis_votes(votes_list):
    votes_list_position = set_position_election(votes_list)
    print('VOTES POSITION')
    count = get_count_position(votes_list_position)
    print('COUNT POSITION')
    show_plot(count)