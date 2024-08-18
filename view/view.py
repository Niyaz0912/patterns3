
class ArticleView:
    def __init__(self, controller):
        self.controller = controller

    def show_information(self):
        information = self.controller.get_information()
        print("Информация о статье:")
        for key, value in information.items():
            print(f"{key}: {value}")

    def update_summary(self, new_summary):
        self.controller.update_summary(new_summary)
        print("Краткое описание обнавлено.")