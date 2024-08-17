class Article:
    def __init__(self, title, author, character_count, publication, summary):
        self.title = title
        self.author = author
        self.character_count = character_count
        self.publication = publication
        self.summary = summary

    def get_information(self):
        return {
            "title": self.title,
            "author": self.author,
            "character count": self.character_count,
            "publication": self.publication,
            "summary": self.summary,
        }

    def update_character_count(self, new_count):
        self.character_count = new_count

    def update_summary(self, new_summary):
        self.summary = new_summary
