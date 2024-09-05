from django.db import models


# Создание новой таблицы с названием Post
class Post(models.Model):

    LIKE_OR_DISLIKE = (
        ('👍🏻', '👍🏻'),
        ('👎🏻', '👎🏻'),

    )

    title = models.CharField(max_length=255,
                             verbose_name='enter title news')
    image = models.ImageField(upload_to='post/',
                              verbose_name='download picture')
    description = models.TextField(verbose_name='white your news')
    url_news = models.URLField(verbose_name='white your url news')
    email_news = models.EmailField(verbose_name='white  email news company')
    #Если вы после миграций забыли указать какое то поле то так же создаете его,
    # но в атрибуте нового поля, указываете null=True и заново проводите миграции (PS: даже если вы изменили название поля)
    like_or_dislike = models.CharField(max_length=100, choices=LIKE_OR_DISLIKE,
                                       null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.created_at}'





