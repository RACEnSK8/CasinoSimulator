import abc
""" Interface for classes that supply statistics """


class StatisticsInterface(metaclass=abc.ABCMeta):
    """Returns a dictionary of statistics"""

    @abc.abstractmethod
    def GetStats(self) -> dict:
        raise NotImplementedError
