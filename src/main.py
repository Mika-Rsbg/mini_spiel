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
If you want to start, type in ok."""


class Game:
    def __init__(self):
        pass

    @staticmethod
    def start():
        global init_health, init_energy, init_strength_factor, init_distance_walked, init_food, init_mobs_found
        with open("src/score.json") as f:
            game_score = json.load(f)
        if len(list(game_score)) == 0:
            init_health = 200
            init_energy = 200
            init_strength_factor = 1.0
            init_distance_walked = 0
            init_food = 15
            init_mobs_found = 0
        else:
            for x in game_score.keys():
                exec("{fx} = {fvalue}".format(fx=x, fvalue=game_score[x]))

    def restart(self):
        pass

    def stop(self):
        pass

    def kill(self):
        pass


class Interaction(Game):
    def __init__(self):
        Game.__init__(self)

    @staticmethod
    def title_screen():
        print(welcome_message)
        if input(":").lower() == "ok":
            print("Alright, let's start!")

    def action_request(self):
        pass

    def response(self):
        pass

    def end_screen(self):
        pass

    def death_screen(self):
        pass


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
        pass

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
    game.start()
    gameInteraction.title_screen()
