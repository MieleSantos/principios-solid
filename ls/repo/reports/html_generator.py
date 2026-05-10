from repo.reports.base_generator import ReportGenerator


class HTMLGenerator(ReportGenerator):
    @classmethod
    def build(cls, repos):
        if not repos:
            return []
        items = " ".join(
            f"<strong>ID: </strong>{repo._id}<strong>NAME: </strong> {repo._name} <strong>stars: </strong>{repo._stars} \n "
            for repo in repos
        )
        return [f"<p>{items}"]
