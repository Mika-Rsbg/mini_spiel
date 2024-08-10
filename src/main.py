import json
from random import randint
init_health = None
init_energy = None
init_strength_factor = None
init_distance_walked = None
init_food = None
init_mobs_found = None


welcome_message = """
Hey there! Welcome to our little Game, little Game!

Additional information is found on our GitHub.
If you want to load the last game, type in "load".
If you want to start a new game, type "new"."""


class Game:
    def __init__(self):
        pass

    @staticmethod
    def start(method):
        global init_health, init_energy, init_strength_factor, init_distance_walked, init_food, init_mobs_found
        if method == "new":
            init_health = 200
            init_energy = 200
            init_strength_factor = 1.0
            init_distance_walked = 0
            init_food = 15
            init_mobs_found = 0
        elif method == "load":
            with open("src/score.json") as f:
                game_score = json.load(f)
            for x in game_score.keys():
                exec("{fx} = {fvalue}".format(fx=x, fvalue=game_score[x]))

    def restart(self):
        pass

    def stop(self):
        pass

    def kill(self):
        pass


# noinspection PyArgumentList
class Interaction(Game):
    def __init__(self):
        Game.__init__(self)

    @staticmethod
    def title_screen():
        print(welcome_message)
        user_in = input(": ")
        if user_in.lower() == "load":
            Game.start("load")
        elif user_in.lower() == "new":
            Game.start("new")

    @staticmethod
    def request_action():
        print("W/w to walk")
        print("E/e to eat")
        print("-----------")
        player_input = input("What do you wanna do:")
        return player_input

    @staticmethod
    def execute_action(action_id):
        if action_id == "w" or action_id == "W":
            player.walk()
        if action_id == "e" or action_id == "E":
            player.eat()

    def request_food(self):
        pass

    def response(self):
        pass

    def end_screen(self):
        pass

    def death_screen(self):
        pass


# noinspection PyArgumentList
class Player:
    def __init__(self):
        self.health = init_health
        self.energy = init_energy
        self.distance_walked = init_distance_walked
        self.food = init_food
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
        # "food" is not the final variable name
        food = Interaction.request_food()
        self.food -= 1
        # self.energy +=

    def item_found(self):
        pass

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


class Item:
    def __init__(self):
        pass

    def item_found(self):
        pass


if __name__ == "__main__":
    game = Game
    gameInteraction = Interaction
    player = Player
    item = Item
    monster = Monster
    playerFight = Fight
    gameInteraction.title_screen()
