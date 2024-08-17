class ArticleController:
    def __init__(self, article):
        self.article = article

    def get_information(self):
        return self.article.get_information()

    def update_character_count(self, new_count):
        self.article.update_character_count(new_count)

    def update_summary(self, new_summary):
        self.article.update_summary(new_summary)