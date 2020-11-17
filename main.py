from build_graph import set_position_election, get_count_position, show_plot
from get_votes import president_2018_brazil, get_votes_list

vot = president_2018_brazil()
votes_list = get_votes_list(vot)

votes_list_position = set_position_election(votes_list)
count = get_count_position(votes_list_position)
show_plot(count)