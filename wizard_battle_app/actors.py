import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of level {} ".format(
            self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level
        # creature_roll = random.randint(1, 12) * creature.level
        creature_roll = creature.get_defensive_roll()

        print('You roll {}...'.format(my_roll))
        print('The {} rolls {}'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard {} has handily triumphed over the {} '.format(self.name, creature.name))
            return True
        else:
            print('The wizard {} has been DEFEATED!!! '.format(self.name))
            return False




class SmallAnimal(Creature):
    pass

class Dragon(Creature):
    pass