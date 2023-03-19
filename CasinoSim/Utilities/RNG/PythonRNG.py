from random import randint

from CasinoSim.Utilities.RNG.RNGInterface import RNGInterface

""" Random Number Generator implemented with standard python random library """


class PythonRNG(RNGInterface):
    def RandomInt(self, lower: int, upper: int) -> int:
        return randint(lower, upper)
