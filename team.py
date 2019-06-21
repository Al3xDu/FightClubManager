"""
Classes:
- Manager
- Team of fighters
- Tournament/League
- Fighters
- Skill level
Stamina
Streghth
Inteligence
- Salary
- Arena(Game)
"""
import random
import copy


class Team:
    """
    - a team has many fighters
    - a team has a ranking in a league
    - a team wins/losses matches in a league
    - a team has a single manager
    """
    def __init__(self, name):
        self.name = name
        self.fighters = []

        self.wins = 0
        self.losses = 0

    def rating(self):
        """
        what is the rating of the team
        """
        rating = 0
        for fighter in self.fighters:
            rating += fighter.skill
        return rating

    def __str__(self):
        return '{} {}'.format(self.name, self.rating())

class Manager:
    """
    - a manager runs the team(manage fighters, hire and fire, look at stats, etc)
    """
    pass


class Game:
    """
    - plays a match between two fighters of diferent teams
    - the fighters are chosen at random between the two teams
    - an arena(game) belongs to a league
    """
    def __init__(self, league, home_team, away_team):
        self.league = league

        self.home_team = home_team
        self.away_team = away_team

        self.home_team_won = None

        print('{} vs. {} '.format(self.home_team, self.away_team))

    def play(self):
        """
        play the game and return the one who won
        True means the home team won, False means the away team won
        """
        print('Match begins')

        # insert match here

        print('Match ends')

        if self.home_team.rating() > self.away_team.rating():
            print('{} wins'.format(self.home_team))
            self.home_team_won = True
        else:
            print('{} wins'.format(self.away_team))
            self.home_team_won = False
        return True


class League:
    """
    - a league has many teams
    - each team is gonna have a ranking within every single league
    """
    def __init__(self, name):
        self.name = name
        self.teams = []

    def set_teams(self, teams):
        # finish the current league season
        self.teams = teams

    def play_tournament(self):
        """
        play 10 rounds between all our teams
        """
        print('Tournament begins.')
        for i in range(10):
            self.play_round()
        print('Tournament ends.')

    def play_round(self):
        """
        play a round, which is 3 matches
        """
        print('Round begins.')
        num_teams = len(self.teams)
        num_games = num_teams // 2

        teams_to_play = copy.copy(self.teams)
        for game_num in range(num_games):
            home_team = random.choice(teams_to_play)
            teams_to_play.remove(home_team)
            away_team = random.choice(teams_to_play)
            teams_to_play.remove(away_team)

            game = Game(self, home_team, away_team)
            game.play()
            self.resolve_game(game)

        print('Round ends.')

        print('Ladder:')
        #ladder status for the team
        self.ladder()

    def ladder(self):
        for team in sorted(self.teams, key =lambda t: -t.wins):
            print('{}: {} wins.'.format(team, team.wins))

    def resolve_game(self, game):
        if game.home_team_won:
            # home team won
            game.home_team.wins += 1
            game.away_team.losses += 1
        else:
            # away team won
            game.home_team.losses += 1
            game.away_team.wins += 1
