class MarkdownGenerator:
    def build(self, repos):
        items = " ".join(
            f"**ID:**{repo.id} **NAME:** {repo.name} **stars:** {repo.stars} \n "
            for repo in repos
        )
        return f"## REPOS \n\n {items}"
