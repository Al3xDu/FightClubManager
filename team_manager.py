class TeamManager:
    """
    - a manager runs the team(manage fighters, hire and fire, look at stats, etc)
    """
    def __init__(self, team, league, ):
        self.team = team
        self.league = league

        self.inputs = {
            1: self.view_fighters,
            2: self.next_round
        }
        self.finished = False

        print('You are a manager.')
        print('You manage the {}.'.format(self.team))
        print('Good luck!')

    def manage(self):
        """
        before every round we can make changes as a manager
        """
        print('')

        print('Your team is {}.'.format(self.team))
        print('You have {} wins out of {} games.'.format(self.team.wins,
                                                         self.league.rounds_played))
        print('You currently have ${}.'.format(self.team.money))
        print('')
        while not self.finished:
            self.print_menu()
            selection = input('Make selection :')
            # does some strange things (wtf) ???
            action = self.inputs.get(int(selection), None)
            if action is None:
                print('Invalid selection !')
            else:
                print('')
                action()
                print('')

        print('')

    def print_menu(self):
        print('1. View your team of fighters.')
        print('2. Play the next round.')

    def view_fighters(self):
        print('fighters')

    def next_round(self):
        print('next round')
        self.finished = True
