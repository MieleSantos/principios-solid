from github.client import GithubClient
from parser import RepoParser
from repo.reports_generator import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator


if __name__ == "__main__":
    username = "Mielesantos"
    response = GithubClient.get_repos_by_user(username)

    if response.get("status_code") == 200:
        repos = RepoParser.parse(response["body"])

        # DIP aplicado: dependências injetadas de fora
        # ReportsGenerator depende da abstração ReportGenerator, não de implementações concretas
        generator = ReportsGenerator([HTMLGenerator(), MarkdownGenerator()])

        for report in generator.build_all(repos):
            print(report)
            print("---")

        # Fácil de adicionar novos formatos sem modificar ReportsGenerator
        # Basta criar uma nova classe que implemente ReportGenerator
    else:
        print(response["body"])
