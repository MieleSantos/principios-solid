from repo.reports.report_generator import ReportGenerator


class MarkdownGenerator(ReportGenerator):
    def build(self, repos):
        items = " ".join(
            f"**ID:**{repo.id} **NAME:** {repo.name} **stars:** {repo.stars} \n "
            for repo in repos
        )
        return f"## REPOS \n\n {items}"
