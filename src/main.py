init_health = 200
init_energy = 200
init_distance_to_treasure = 100
init_food = 15
init_mobs_found = 0


class Player:
    def __init__(self):
        self.health = init_health
        self.energy = init_energy
        self.distance_to_treasure = init_distance_to_treasure
        self.food = init_food
        self.mobs_found = init_mobs_found

    def walking(self):
        pass

    def eating(self):
        pass

    def animal_found(self):
        pass

    def mob_found(self):
        pass

    def fighting(self):
        pass

    def treasure(self):
        pass

    def restart(self):
        pass
