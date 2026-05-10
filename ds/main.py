from github.client import GithubClient
from parser import RepoParser
from repo.reports_generator import ReportsGenerator


if __name__ == "__main__":
    username = "Mielesantos"
    response = GithubClient.get_repos_by_user(username)

    if response.get("status_code") == 200:
        repos = RepoParser.parse(response["body"])

        # Violação DIP: ReportsGenerator instancia dependências concretas internamente
        # Para adicionar um novo formato, precisa modificar a classe
        generator = ReportsGenerator()
        print(generator.build_html(repos))
        print(generator.build_markdown(repos))
    else:
        print(response["body"])
