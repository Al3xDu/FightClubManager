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
    def play(self):
        return None

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
        for i in range(10):
            self.play_round()

    def play_round(self):
        """
        play a round, which is 3 matches
        """
        num_teams = len(self.teams)
        num_games = num_teams // 2

        teams_to_play = copy.copy(self.teams)
        for game_num in range(num_games):
            home_team = random.choice(teams_to_play)
            teams_to_play.remove(home_team)
            away_team = random.choice(teams_to_play)
            teams_to_play.remove(away_team)

            game = Game(self,home_team, away_team )
            game.play()
