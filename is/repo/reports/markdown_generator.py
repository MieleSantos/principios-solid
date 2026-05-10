from repo.reports.report_generator import ReportGenerator


class MarkdownGenerator(ReportGenerator):
    def build_html(self, repos):
        raise NotImplementedError("MarkdownGenerator nao suporta html")

    def build_markdown(self, repos):
        items = " ".join(
            f"**ID:**{repo.id} **NAME:** {repo.name} **stars:** {repo.stars} \n "
            for repo in repos
        )
        return f"## REPOS \n\n {items}"

    def save_to_file(self, content, path):
        raise NotImplementedError("MarkdownGenerator nao salva em arquivo")
