from controller.controller import ArticleController
from model.model import Article
from view.view import ArticleView

# Создаем экземпляр статьи
article = Article(
    title="Охрана окружающей среды, как объект государственного управления",
    author="И.А. Игнатьева",
    character_count=18000,
    publication="CyberLeninka",
    summary="Краткая информация о статье"
)

# Контроллер для статьи
controller = ArticleController(article)

# Создаем представление для отображения информации
view = ArticleView(controller)

# Показываем информацию о статье
view.show_information()

# Обнавляпем сводку
new_summary = "Статья рассматривает охрану окружающей и негативное на него воздействие хозяйственной деятельности человека."
view.update_summary(new_summary)
view.show_information()