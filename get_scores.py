from prettytable import PrettyTable
from pycricbuzz import *
from json import dumps
from pretty_status import pretty_status

def display_match_score():
    client = Cricbuzz()
    matches = client.matches()

    recent_matches = PrettyTable(['S.No', 'Match Description', 'Series', 'Current Status'])
    recent_matches.align = 'l'

    for match_no,match in enumerate(matches):
        recent_matches.add_row([match_no+1, match['mchdesc'], match['srs']+"("+match['mnum']+")", pretty_status[match['mchstate']]])

    print recent_matches

    match_request = int(raw_input('Which match do you want updates for:  '))
    match_info(client, matches[match_request-1])


def match_info(client, match):
    if match['mchstate'] in ["inprogress"]:

        current_match = client.livescore(match['id'])

        if not current_match['batting']['score'] and not current_match['bowling']['score']:
            print current_match['matchinfo']['status']

        else:
            print '{}: {}/{} ({} ov),'.format(current_match['batting']['team'], current_match['batting']['score'][0]['runs'], current_match['batting']['score'][0]['wickets'], current_match['batting']['score'][0]['overs']),

            for batsman in current_match['batting']['batsman']:
                print '{}: {}({}) '.format(batsman['name'], batsman['runs'], batsman['balls']),

            for bowlers in current_match['bowling']['bowler']:
                if bowlers['name'][-1]=='*':
                    bowlers['name'] = bowlers['name'][:-1]
                print '{}: {}-{}-{}-{} '.format(bowlers['name'], bowlers['overs'], bowlers['maidens'], bowlers['runs'], bowlers['wickets']),

            print '\n'

if __name__ == '__main__':
    display_match_score()
