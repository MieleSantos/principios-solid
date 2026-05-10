from repo.reports.base_generator import ReportGenerator


class MarkdownGenerator(ReportGenerator):
    @classmethod
    def build(cls, repos):
        items = " ".join(
            f"**ID:**{repo._id} **NAME:** {repo._name} **stars:** {repo._stars} \n "
            for repo in repos
        )
        return f"## REPOS \n\n {items}"

    @classmethod
    def build_with_header(cls, repos, header):
        items = " ".join(
            f"**ID:**{repo._id} **NAME:** {repo._name} **stars:** {repo._stars} \n "
            for repo in repos
        )
        return f"## {header} \n\n {items}"
