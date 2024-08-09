init_health = 200
init_energy = 200
init_strength_factor = 1.0
init_distance_walked = 0
init_food = 15
init_mobs_found = 0


class Game:
    def __init__(self):
        pass

    def start(self):
        pass

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
