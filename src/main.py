import json
init_health = None
init_energy = None
init_strength_factor = None
init_distance_walked = None
init_food = None
init_mobs_found = None


class Game:
    def __init__(self):
        pass

    @staticmethod
    def start():
        global init_health, init_energy, init_strength_factor, init_distance_walked, init_food, init_mobs_found
        with open("score.json", "r") as f:
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


class Player:
    def __init__(self):
        self.health = init_health
        self.energy = init_energy
        self.distance_walked = init_distance_walked
        self.food = init_food
        self.mobs_found = init_mobs_found

    def walk(self):
        pass

    def eat(self):
        pass

    def animal_found(self):
        pass

    def mob_found(self):
        pass

    def item_found(self):
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


if __name__ == "__main__":
    game = Game
    player = Player
    game.start()
