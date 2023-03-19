from CasinoSim.Utilities.RNG.PythonRNG import PythonRNG
from CasinoSim.Utilities.RNG.RNGInterface import RNGInterface
from CasinoSim.Utilities.Statistics.StatisticsInterface import \
    StatisticsInterface

""" Implementation of a single die """


class Die(StatisticsInterface):
    """Initialization of the die"""

    def __init__(self, sides: int = 6, rng: RNGInterface = PythonRNG()):
        self.sides = sides
        self.rng = rng
        self.history = []

    """ Rolls the die and returns the value of the roll """

    def Roll(self) -> int:
        value = self.rng.RandomInt(1, self.sides)
        self.history.append(value)
        return value

    """ StatisticsInterface implementation """

    def GetStats(self) -> dict:
        ret = {"rollHistory": self.history}
        return ret


if __name__ == "__main__":
    print("Rolling a default die 10 times")
    die = Die()
    for i in range(0, 10):
        die.Roll()
    print(die.GetStats()["rollHistory"])

    print("Rolling a 20-sided die 10 times")
    die = Die(sides=20)
    for i in range(0, 10):
        die.Roll()
    print(die.GetStats()["rollHistory"])
