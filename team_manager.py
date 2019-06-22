from helpers import select_from_menu, print_menu


class TeamManager:
    """
    - a manager runs the team(manage fighters, hire and fire, look at stats, etc)
    """
    def __init__(self, team, league, ):
        self.team = team
        self.league = league

        self.inputs = {
            1: self.view_fighters,
            2: self.view_market,
            3: self.trade_fighters,
            4: self.next_round
        }
        self.finished = False

        print('You are a manager.')
        print('You manage the {}.'.format(self.team))
        print('Good luck!')

    def manage(self):
        """
        before every round we can make changes as a manager
        """
        self.finished = False
        print('')

        print('Your team is {}.'.format(self.team))
        print('You have {} wins out of {} games.'.format(self.team.wins,
                                                         self.league.rounds_played))
        print('You currently have ${}.'.format(self.team.money))
        print('Your team salary is ${} a week.'.format(self.team.weekly_salary()))
        print('')
        while not self.finished:
            print_menu()
            select_from_menu(self.inputs)

        print('')


    def view_market(self):
        for i, fighter in enumerate(self.league.fighters):
            print('{}. {}'.format(i, fighter))

    def view_fighters(self):
        for i, fighter in enumerate(self.team.fighters):
            print('{}. {}'.format(i, fighter))

    def trade_fighters(self):
        """
        switch a fighter on a team for a marketplace fighter
        """
        # select a fighter from your team
        self.view_fighters()
        fighter_index = int(input('Which fighter do you want to switch?:'))
        print('')
        # select a fighter from the market
        self.view_market()
        market_index = int(input('Which fighter do you want to hire?:'))
        print('')
        # change them
        print('Switching {} for {}.'.format(
            self.team.fighters[fighter_index],
            self.league.fighters[market_index]
        ))
        fighter_from_team = self.team.fighters.pop(fighter_index)
        fighter_from_market = self.league.fighters.pop(market_index)

        self.team.fighters.append(fighter_from_market)
        self.league.fighters.append(fighter_from_team)

    def next_round(self):
        print('next round')
        self.finished = True
