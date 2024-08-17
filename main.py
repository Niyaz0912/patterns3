from controller.controller import ArticleController
from model.model import Article
from viev.viev import ArticleView

# Создаем экземпляр статьи
article = Article(
    title="Programming in Python",
    author="John Doe",
    character_count=1500,
    publication="Programming for Everyone",
    summary="An introduction to the basics of programming in Python."
)

# Контроллер для статьи
controller = ArticleController(article)

# Создаем представление для отображения информации
view = ArticleView(controller)

# Показываем информацию о статье
view.show_information()

# Обнавляпем сводку
view.update_summary("Updated summary of the article about Python.")
view.show_information()