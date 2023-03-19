import abc
""" Interface that all available Random Number Generators need to implement """


class RNGInterface(metaclass=abc.ABCMeta):
    """Acquire a random integer between [lower, upper] including both endpoints"""

    @abc.abstractmethod
    def RandomInt(self, lower: int, upper: int) -> int:
        raise NotImplementedError
