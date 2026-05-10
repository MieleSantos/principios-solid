class ReportsGenerator:
    def __init__(self, formatter):
        self._formatter = formatter

    def build(self, repos):
        return self._formatter.format(repos)
