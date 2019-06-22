import random


def select_from_menu(menu_options: dict):
    selection = input('Make selection :')
    # does some strange things,but works lol (wtf) ???
    action = menu_options.get(int(selection), None)
    if action is None:
        print('Invalid selection !')
    else:
        print('')
        action()
        print('')


def resolve_game(game):
    if game.home_team_won:
        # home team won
        game.home_team.wins += 1
        game.away_team.losses += 1
        game.home_team.money += round(100000 * random.random())
    else:
        # away team won
        game.home_team.losses += 1
        game.away_team.wins += 1
    game.home_team.pay_fighters()
    game.away_team.pay_fighters()
    game.away_team.money += round(100000 * random.random())


def print_menu():
    print('1. View your team of fighters.')
    print('2. View the fighters on the market.')
    print('3. Trade fighters.')
    print('4. Play the next round.')
