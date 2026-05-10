from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator


class ReportsGenerator:
    @classmethod
    def build(cls, generator, repos):
        return generator.build(repos)
