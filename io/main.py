from github.client import GithubClient
from parser import RepoParser
from repo.reports_generator import ReportsGenerator
from repo.reports.html_formatter import HTMLFormatter
from repo.reports.markdown_formatter import MarkdownFormatter
from repo.reports.file_saver import FileSaver


if __name__ == "__main__":
    username = "Mielesantos"
    response = GithubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])

        html_report = ReportsGenerator(HTMLFormatter())
        markdown_report = ReportsGenerator(MarkdownFormatter())

        print(html_report.build(repos))
        print(markdown_report.build(repos))

        # Cada classe implementa só o que precisa
        saver = FileSaver()
        saver.save(html_report.build(repos), "/tmp/report.html")
        print("Arquivo salvo com sucesso")
    else:
        print(response["body"])
