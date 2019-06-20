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


class Manager:
    """
    - a manager runs the team(manage fighters, hire and fire, look at stats, etc)
    """
    pass


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


class Game:
    """
    - plays a match between two fighters of diferent teams
    - the fighters are chosen at random between the two teams
    - an arena(game) belongs to a league
    """
    pass
