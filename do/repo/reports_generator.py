from collections.abc import Sequence
from repo.reports.report_generator import ReportGenerator


class ReportsGenerator:
    def __init__(self, generators: Sequence[ReportGenerator]):
        self._generators = generators

    def build_all(self, repos):
        return [g.build(repos) for g in self._generators]
