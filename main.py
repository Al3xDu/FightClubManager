from fighter import generate_fighter
from team import League, Team

import random


def main():
    # set up our data
    # generate some players, random(a couple hundred)
    fighters = []
    for i in range(100):
        fighters.append(generate_fighter())
    # set up 5 teams
    teams = [
        Team('Avengers'),
        Team('Annihilators'),
        Team('Black Panthers'),
        Team('Brute Force'),
        Team('Chaos'),
        Team('Full Atack')
    ]
    for team in teams:
        for fighter_num in range(5):
            # 5 fighters given from start at random
            selected_fighter = random.choice(fighters)
            team.fighters.append(selected_fighter)
            fighters.remove(selected_fighter)
    # create random fighters, create random managers(the player is one of those managers)
    first_league = League('Battle Zone')
    first_league.set_teams(teams)

    first_league.play_tournament()


if __name__ == '__main__':
    main()
