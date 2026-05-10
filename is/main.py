from github.client import GithubClient
from parser import RepoParser
from repo.reports_generator import ReportsGenerator


if __name__ == "__main__":
    username = "mielesantos"
    response = GithubClient.get_repos_by_user(username)

    if response.get("status_code") == 200:
        repos = RepoParser.parse(response["body"])
        generator = ReportsGenerator()

        print(generator.build_html(repos))
        print(generator.build_markdown(repos))

        # Violação ISP: HTMLGenerator tem métodos que não fazem sentido
        # O código compila, mas lança NotImplementedError em tempo de execução
        try:
            generator._html.save_to_file("conteudo", "/tmp/report.html")
        except NotImplementedError as e:
            print(f"Erro esperado: {e}")
    else:
        print(response["body"])
