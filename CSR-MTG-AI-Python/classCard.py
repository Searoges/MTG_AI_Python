class Card(object):
    def __init__(self):
        self.name = ""  # Card name
        self.CMC = [0,0,0,0,0,0,0]  # White Blue Black Red Green Colourless Generic
        self.types = []  # All types i.e. Erebos is an Enchantment Creature
        self.subtypes = []  # All subtypes i.e. Beast Caller Savnt is an Elf, Shaman, Ally
        self.keywords = []  # All keywords i.e. Trample
        self.target = ""  # Target for targeted abilities and if blocked blocker(s) become target
        self.tapped = False  # Is this card tapped
        self.permanent = True # Stays in play
        self.colourIdentity = []  # Array of all colours in the cards colour identity


class Creature(Card):
    def __init__(self):
        self.power = 0  # Power
        self.currentPower = self.power # Current Power
        self.toughness = 0  # Toughness
        self.currentToughness = self.toughness  # Current Toughness
        self.summoningSickness = True  # Cannot be tapped the turn it enteres
        self.plusOneCounters = 0  # Number of +1/+1 counters on creature
        self.minusOneCounters = 0 # Number of -1/-1 counters on creature

class Land(Card):
    def __init__(self):
        self.produces = []  # All colours that the land produces
        self.basic = True  # Is it a basic land

class Instant(Card):
    def __init__(self):

class Sorcery(Card):
    def __init__(self):

class Artifact(Card):
    def __init__(self):

class Planeswalker(Card):
    def __init__(self):
        self.Loyaty = 0  # Starting Loyalty Points
        self.abilities = [[]]  # Planeswalker Loyalty Abilities
