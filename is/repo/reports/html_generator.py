from repo.reports.report_generator import ReportGenerator


class HTMLGenerator(ReportGenerator):
    def build_html(self, repos):
        items = " ".join(
            f"<strong>ID: </strong>{repo.id}<strong>NAME: </strong> {repo.name} <strong>stars: </strong>{repo.stars} \n "
            for repo in repos
        )
        return f"<p>{items}"

    def build_markdown(self, repos):
        raise NotImplementedError("HTMLGenerator nao suporta markdown")

    def save_to_file(self, content, path):
        raise NotImplementedError("HTMLGenerator nao salva em arquivo")
