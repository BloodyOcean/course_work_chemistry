import abc


class Generator(abc.ABC):
    @abc.abstractmethod
    def next(self) -> str:
        pass
