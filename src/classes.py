import json
import sys
from random import randint
import os

init_health = None
init_energy = None
init_strength_factor = None
init_distance_walked = None
init_food = None
init_items = None
init_mobs_found = None

enableClearingTerminalScreen = True

init_dict_responses = {}

welcome_message = """
Hey there! Welcome to our little Game, Mini Game!

Additional information is found on our GitHub."""


class Game:
    def __init__(self):
        self.dict_responses = init_dict_responses

    @staticmethod
    def start():
        global init_health, init_energy, init_strength_factor, init_distance_walked, init_food, init_mobs_found, init_items, player
        method = gameInteraction.getPlayerResponse("""Wanna start a new game ("new") or load an existing ("load")""")
        if method == "new":
            init_health = 200
            init_energy = 200
            init_strength_factor = 1.0
            init_distance_walked = 0
            init_food = {"food": 15}
            init_items = {"item": 0}
            init_mobs_found = 0
            player = Player()
        elif method == "load":
            try:
                with open("src/score.json", "r") as f:
                    game_score = json.load(f)
                if len(list(game_score)) < 7:
                    gameInteraction.notifyPlayer("text", "The JSON File is not big enough, some values are missing")
                else:
                    init_health = game_score.get("init_health", 200)
                    init_energy = game_score.get("init_energy", 200)
                    init_strength_factor = game_score.get("init_strength_factor", 1.0)
                    init_distance_walked = game_score.get("init_distance_walked", 0)
                    init_food = game_score.get("init_food", {"food": 15})
                    init_items = game_score.get("init_items", {"item": 0})
                    init_mobs_found = game_score.get("init_mobs_found", 0)
                player = Player()
            except Exception as e:
                gameInteraction.notifyPlayer("text", """Failed, the file might not exist.
                Error code:{ferror}""".format(ferror=e))
                Game.start()

    def restart(self):
        game.stop()
        game.start()

    @staticmethod
    def stop():
        gameInteraction.end_screen()
        json_data = {
            "init_health": player.health,
            "init_energy": player.energy,
            "init_strength_factor": player.strength_factor,
            "init_distance_walked": player.distance_walked,
            "init_food": player.food,
            "init_items": player.items,
            "init_mobs_found": player.mobs_found
        }
        with open("src/score.json", "w") as f:
            json.dump(json_data, f)
        gameInteraction.kill()

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
        action_id = gameInteraction.getPlayerResponse("""What do you wanna do?
"w" to walk
"e" to eat
"s" to stop the game
""")

        if action_id.lower() == "w":
            player.walk()
        if action_id.lower() == "e":
            player.eat()
        if action_id.lower() == "s":
            Game.stop()

    @staticmethod
    def request_food():
        food_energy = 5
        return food_energy

    def notifyPlayer(t, content, self):
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
        gameInteraction.notifyPlayer("text", "stop_message")

    def death_screen(self):
        pass


class Player:
    def __init__(self):
        self.health = int(init_health)
        self.energy = int(init_energy)
        self.strength_factor = float(init_strength_factor)
        self.distance_walked = int(init_distance_walked)
        self.food = init_food
        self.items = init_items
        self.mobs_found = int(init_mobs_found)

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
        self.items["item"] += 1

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
