from repo.reports.saver import Saver


class FileSaver(Saver):
    def save(self, content, path):
        with open(path, "w") as f:
            f.write(content)
