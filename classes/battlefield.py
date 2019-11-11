from .units.solider import Solider
from .units.vehicle import Vehicle
from .formations.squad import Squad
from .formations.army import Army
from random import randint, choice, shuffle
from .rand import Rand
from .strategy import STRATEGIES
from json import load
from typing import Optional


ARMY_NAMES = [
    'The Ruthless Ravagers',
    'The Cluster',
    'The Hell Hosts',
    'The Death Pack',
    'The Myriad',
    'The Eclipse',
    'The Gexamp',
    'The Maron',
    'The Akharid',
    'The Aflobax'
    ]


class Battlefield:
    def __init__(self, armies: list) -> None:
        self.armies = armies

    def battle(self):
        print('The following armies take part in the battle:')
        for army in self.armies:
            print(f'\t{army.name} (Stratrgy: '
                  f'{army.strategy.__class__.__name__}).')

        move_counter = 0
        while len(self.active_armies) > 1:
            move_counter += 1
            print('Move: ', move_counter)
            for attacking_army in self.active_armies:
                enemy_army = Rand.choice([army for army in self.active_armies
                                          if army is not attacking_army])
                attacking_army.attack(enemy_army)
        print('Number of moves: ', move_counter)
        print('Winner: ', self.active_armies[0].name)

    @classmethod
    def create_new_buttlefield(cls) -> object:
        seed = randint(0, 1000)
        Rand.seed(seed)
        armies = list()
        for i in range(3):
            shuffle(ARMY_NAMES)
            name = ARMY_NAMES[0]
            strategy = choice(list(STRATEGIES.keys()))
            ARMY_NAMES.pop(0)
            armies.append(cls.create_army(strategy, name))
        return cls(armies)

    @classmethod
    def create_battlefield_from_config(cls) -> object:
        try:
            with open('config/config.json', 'r') as json_file:
                config = load(json_file)
        except FileNotFoundError:
            raise FileNotFoundError('Last game not found!')
        Rand.seed(config['seed'])
        armies = list()
        for army in config['armies']:
            armies.append(cls.create_army(army['strategy'],
                                          army['name'], army['squads']))
        return cls(armies)

    @property
    def active_armies(self) -> list:
        return [army for army in self.armies if army.is_active]

    @classmethod
    def create_solider(cls) -> Solider:
        return Solider()

    @classmethod
    def create_vehicle(cls, operator_count: Optional[int] = None) -> Vehicle:
        operators = list()
        if not operator_count:
            operator_count = randint(1, 3)
        for i in range(operator_count):
            operators.append(cls.create_solider())
        return Vehicle(operators)

    @classmethod
    def create_squad(cls, units_data: Optional[list] = None) -> Squad:
        units = list()
        if not units_data:
            units_data = list()
            units_count = randint(5, 10)
            for i in range(units_count):
                units_data.append({'type': choice(['Solider', 'Vehicle'])})
        else:
            units_data = units_data['units']
        for unit in units_data:
            if unit['type'] == 'Solider':
                units.append(cls.create_solider())
            elif unit['type'] == 'Vehicle':
                if 'operators' in unit:
                    operator_count = len(unit['operators'])
                else:
                    operator_count = None
                units.append(cls.create_vehicle(operator_count))
        return Squad(units)

    @classmethod
    def create_army(cls, strategy: str, name: str,
                    squads_data: Optional[list] = None) -> object:
        squads = list()
        if not squads_data:
            squads_count = randint(2, 5)
            squads_data = [None for i in range(squads_count)]
        for squad in squads_data:
            squads.append(cls.create_squad(squad))
        return Army(squads, strategy, name)
