class HTMLGenerator:
    def build(self, repos):
        items = " ".join(
            f"<strong>ID: </strong>{repo.id}<strong>NAME: </strong> {repo.name} <strong>stars: </strong>{repo.stars} \n "
            for repo in repos
        )
        return f"<p>{items}"
