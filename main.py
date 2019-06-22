from fighter import generate_fighter
from team import League, Team
from team_manager import TeamManager

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
    first_league = League('Battle Zone', teams, fighters)
    first_league.set_teams(teams)

    # create the manager(player)
    manager = TeamManager(random.choice(teams), first_league)

    """
    play 10 rounds between all our teams
     """
    print('Tournament begins.')
    for i in range(10):
        manager.manage()
        first_league.play_round()
    print('Tournament ends.')


if __name__ == '__main__':
    main()
