from adventurelib import Item, say
from random import choice
class Character(Item):
    def __init__(self, name, desc, hp, dp, powers=None, exp=None):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.dp = dp
        self.powers = powers
        self.exp = exp

class Player(Character):
    def __init__(self, name, hp, dp, powers=None, exp=None, lvl=None):
        self.name = name
        self.hp = hp
        self.dp = dp
        self.powers = powers
        self.exp = exp
        self.lvl = lvl


class Battle():
    def __init__(self, lose_msg, win_msg, character_, player_, reset_func):
        self.lose_msg = lose_msg
        self.win_msg = win_msg
        character = character_
        player = player_
        self.reset_func = reset_func

    def start(self):
        finished = False
        while not finished:
            if player.hp <= 0:
                say("You died.")
                
                self.reset_func()
                break
            elif character.hp <= 0:
                say("You won!")
                break
            message = choice(choice([self.win_msg, self.lose_msg]))
            say(f'You are now fighting the {character}')
            response = input(f"HP{player.hp}\nChoose a power")
            if response in player.powers:
                say(f'You {response} the {character.name}')
                character.hp -= player.dp
                say(f"The {character.name} has now {character.hp} health points")
                say(message)
                if message in self.win_msg:
                    player.hp += character.dp
                player.hp -= character.dp
                say(f"The {character.name} fights you back and you lose {character.dp} HP")
            else:
                say("Choose a valid power")
            
            
