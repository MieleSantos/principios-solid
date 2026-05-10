class ReportGenerator:
    def build_html(self, repos):
        raise NotImplementedError

    def build_markdown(self, repos):
        raise NotImplementedError

    def save_to_file(self, content, path):
        raise NotImplementedError
