from github.client import GithubClient
from repo.parser import RepoParser
from repo.reports_generator import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator


if __name__ == "__main__":
    username = "mielesantos"
    response = GithubClient.get_repos_by_user(username)

    if response.get("status_code") == 200:
        repos = RepoParser.parse(response["body"])

        # Violação LSP #1: HTMLGenerator retorna list[], não str
        report = ReportsGenerator.build(HTMLGenerator, repos)
        print(type(report))

        # Violação LSP #2: MarkdownGenerator.build_with_header
        # Quebra a assinatura esperada exige parâmetro extra
        print(MarkdownGenerator.build_with_header(repos, "MEUS REPOS"))
    else:
        print(response["body"])
