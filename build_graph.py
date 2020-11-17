import json
import plotly.graph_objects as go

def get_party():
    with open ('party.json', 'r') as f:
        party_json = json.load(f)
        f.close()
        return party_json

def set_position_election(votes_list):
    party_json = get_party()

    for row in votes_list:
        coalition = row['coalition']
        list_position = []
        res = ''

        for party in party_json:
            if party['abbrev'] in coalition:
                list_position.append(party['position'])

        if len(list_position) > 0:

            if len(list_position) == 2:
                for i in list_position:
                    if 'centre-' in i or 'far-' in i:
                        res = i

            else:
                res = max(set(list_position), key = list_position.count)
        
        else:
            res = list_position

        row.update({'position': res})

    return votes_list

def get_count_position(votes_list_position):
    far_left = centre_left = centre = centre_right = far_right = unknown = 0

    for row in votes_list_position:
        if row['position'] == 'far-left':
            far_left += int(row['num_votes'])
        
        elif row['position'] == 'centre-left':
            centre_left += int(row['num_votes'])

        elif row['position'] == 'centre':
            centre += int(row['num_votes'])

        elif row['position'] == 'centre-right':
            centre_right += int(row['num_votes'])

        elif row['position'] == 'far-right':
            far_right += int(row['num_votes'])

        else:
            unknown += int(row['num_votes'])

    count_position = {
        'far-left': far_left,
        'centre-left': centre_left,
        'centre': centre,
        'centre-right': centre_right,
        'far-right': far_right,
        'unknown': unknown
    }

    return count_position

def show_plot(count):
    labels = [i for i in count.keys()]
    values = [j for j in count.values()]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.show()