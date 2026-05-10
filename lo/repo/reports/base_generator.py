from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    @classmethod
    @abstractmethod
    def build(cls, repos):
        pass
