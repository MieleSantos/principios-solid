from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    @abstractmethod
    def build(self, repos):
        pass
