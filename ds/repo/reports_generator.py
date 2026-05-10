from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator


class ReportsGenerator:
    def __init__(self):
        self._html = HTMLGenerator()
        self._markdown = MarkdownGenerator()

    def build_html(self, repos):
        return self._html.build(repos)

    def build_markdown(self, repos):
        return self._markdown.build(repos)

    def build_all(self, repos):
        return [self._html.build(repos), self._markdown.build(repos)]
