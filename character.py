import enum


class Race(enum.Enum):
    HUMAN = 'Human',
    ELF = 'Elf',
    DRAGONBORN = 'Dragonborn',
    AASIMAR = 'Aasimar',


race_enum_mapping = {
    Race.HUMAN: 'Human',
    Race.ELF: 'Elf',
    Race.DRAGONBORN: 'Dragonborn',
    Race.AASIMAR: 'Aasimar'
}


class CharacterClass(enum.Enum):
    ROGUE = 'Rogue',
    WIZARD = 'Wizard',
    BARBARIAN = 'Barbarian',
    PALADIN = 'Paladin'


class_enum_mapping = {
    CharacterClass.ROGUE: 'Rogue',
    CharacterClass.WIZARD: 'Wizard',
    CharacterClass.BARBARIAN: 'Barbarian',
    CharacterClass.PALADIN: 'Paladin'
}


class Character:
    def __init__(self, name: str, race: Race, char_class: CharacterClass, player_id):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.player_id = player_id
