from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator


class ReportsGenerator:
    def __init__(self):
        self._html = HTMLGenerator()
        self._markdown = MarkdownGenerator()

    def build_html(self, repos):
        return self._html.build_html(repos)

    def build_markdown(self, repos):
        return self._markdown.build_markdown(repos)
