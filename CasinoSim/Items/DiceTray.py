from CasinoSim.Items.Die import Die
from CasinoSim.Utilities.RNG.PythonRNG import PythonRNG
from CasinoSim.Utilities.RNG.RNGInterface import RNGInterface
from CasinoSim.Utilities.Statistics.StatisticsInterface import StatisticsInterface

""" Dice Tray holds many dice, and handles rolling all enabled die at the same time """


class DiceTray(StatisticsInterface):
    def __init__(self, dice: list[Die], rng: RNGInterface = PythonRNG()):
        self.dice = dice
        self.rng = rng
        self.enabled = []
        self.rollHistory = []

    """ Enable a die in the tray via an index """

    def EnableByIndex(self, index: int):
        if index < 0 or index >= len(self.dice):
            raise ValueError("invalid index")
        self.enabled.append(index)
        self.enabled = list(set(self.enabled))

    """ Enable a die in the tray at random """

    def EnableRandom(self):
        not_enabled = [i for i in range(0, len(self.dice)) if i not in self.enabled]
        if len(not_enabled) > 0:
            index = not_enabled[self.rng.RandomInt(0, len(not_enabled) - 1)]
            self.enabled.append(index)

    """ Disable all enabled dice """

    def DisableAll(self):
        self.enabled = []

    """ Roll all enabled dice and update stats """

    def Roll(self) -> list[int]:
        if len(self.enabled) == 0:
            raise Exception("no dice enabled")
        ret = []
        for index in self.enabled:
            ret.append(self.dice[index].Roll())
        self.rollHistory.append(sum(ret))
        return ret

    def GetStats(self) -> dict:
        ret = {"rollHistory": self.rollHistory}
        for index, die in enumerate(self.dice):
            ret[f"rollHistoryDie{index}"] = die.GetStats()["rollHistory"]
        return ret


if __name__ == "__main__":
    print(
        "Creating tray with 4 default dice, selecting 2 at random and rolling 10 times"
    )
    tray = DiceTray(dice=[Die() for i in range(0, 4)])
    for i in range(0, 2):
        tray.EnableRandom()
    print(f"Dice tray enabled: {tray.enabled}")
    for i in range(0, 10):
        tray.Roll()
    print(tray.GetStats())
    print("Disabling all dice in tray, enabling die 0 & 1, re-rolling 10 times")
    tray.DisableAll()
    tray.EnableByIndex(0)
    tray.EnableByIndex(1)
    print(f"Dice tray enabled: {tray.enabled}")
    for i in range(0, 10):
        tray.Roll()
    print(tray.GetStats())
