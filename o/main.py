from github.client import GithubClient
from repo.reports_generator import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MakdownGenerator

if __name__ == "__main__":
    username = "Mielesantos"
    response = GithubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdown_report = ReportsGenerator.build(MakdownGenerator, repos)
        html_report = ReportsGenerator.build(HTMLGenerator, repos)
        print(markdown_report)

        print(html_report)
    else:
        print(response["body"])
