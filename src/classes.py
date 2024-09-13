import json
import sys
from random import randint
import os

init_health = None
init_energy = None
init_strength_factor = None
init_distance_walked = None
init_food = None
init_items = {1: 0, 2: 0}
init_mobs_found = None

enableClearingTerminalScreen = True

init_dict_responses = {}

welcome_message = """
Hey there! Welcome to our little Game, Mini Game!

Additional information is found on our GitHub.
If you want to load the last game, type in "load".
If you want to start a new game, type "new"."""


class Game:
    def __init__(self):
        self.dict_responses = init_dict_responses

    @staticmethod
    def start():
        global init_health, init_energy, init_strength_factor, init_distance_walked, init_food, init_mobs_found, init_items
        method = gameInteraction.getPlayerResponse("""Wanna start a new game ("new") or load an existing ("load")""")
        if method == "new":
            init_health = 200
            init_energy = 200
            init_strength_factor = 1.0
            init_distance_walked = 0
            init_food = 15
            init_items = 0
            init_mobs_found = 0
        elif method == "load":
            try:
                with open("src/score.json") as f:
                    game_score = json.load(f)
                for x in game_score.keys():
                    exec("{fx} = {fvalue}".format(fx=x, fvalue=game_score[x]))
            except Exception as e:
                gameInteraction.notifyPlayer("text", """Failed, the file might not exist.
                Error code:{ferror}""".format(ferror=e))
                game.start()

    def restart(self):
        pass

    @staticmethod
    def stop():
        gameInteraction.notifyPlayer("list", "stop_message")
        json_data = {
            "init_health": player.health,
            "init_energy": player.energy,
            "init_strength_factor": player.strength_factor,
            "init_distance_walked": player.distance_walked,
            "init_food": player.food,
            "init_items": player.items,
            "init_mobs_found": player.mobs_found
        }
        with open("src/score.json") as f:
            json.dump(json_data, f)

    @staticmethod
    def kill():
        sys.exit()


class Interaction(Game):
    def __init__(self):
        Game.__init__(self)

    @staticmethod
    def title_screen():
        print(welcome_message)

    @staticmethod
    def request_action():
        print("W/w to walk")
        print("E/e to eat")
        print("-----------")
        player_input_action_id = input("What do you wanna do:")
        return player_input_action_id

    @staticmethod
    def execute_action(action_id):
        if action_id == "w" or action_id == "W":
            player.walk()
        if action_id == "e" or action_id == "E":
            player.eat()

    @staticmethod
    def request_food():
        food_energy = 5
        return food_energy

    def notifyPlayer(self, t, content):
        """
        :param t: The type of input given ("text" or "list")
        :param content: The content given
        :return: nothing
        """
        if t == "text":
            print("!-----")
            print(content)
        elif t == "list":
            print("!-----")
            print(self.dict_responses[content])

    @staticmethod
    def getPlayerResponse(content):
        """
        :param content: The question to ask
        :return: The players response
        """
        print("?-----")
        playerIn = input(content + " >")
        return playerIn

    @staticmethod
    def clear_terminal():
        global enableClearingTerminalScreen
        if enableClearingTerminalScreen:
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            pass

    def end_screen(self):
        pass

    def death_screen(self):
        pass


class Player:
    def __init__(self):
        self.health = init_health
        self.energy = init_energy
        self.strength_factor = init_strength_factor
        self.distance_walked = init_distance_walked
        self.food = init_food
        self.items = init_items
        self.mobs_found = init_mobs_found

    def walk(self):
        self.distance_walked += 1
        self.energy -= 1

        if randint(1, 100) <= 20:
            self.item_found()

        if randint(1, 100) <= 20:
            self.animal_found()

        if randint(1, 100) <= 20:
            self.mob_found()

    def eat(self):
        food_energie = Interaction.request_food()
        self.food -= 1
        self.energy += food_energie

    def item_found(self):
        rarity_factor = randint(1, 100)
        if rarity_factor <= 10:
            rarity = 2
            self.items[rarity] += 1
        else:
            rarity = 1
            self.items[rarity] += 1

    def animal_found(self):
        pass

    def mob_found(self):
        pass


class Fight(Player):
    def __init__(self):
        Player.__init__(self)

    def attack(self):
        pass

    def defend(self):
        pass


class Monster:
    def run(self):
        pass

    def attack(self):
        pass

    def die(self):
        pass


game = Game()
gameInteraction = Interaction()
player = Player()
monster = Monster()
playerFight = Fight()