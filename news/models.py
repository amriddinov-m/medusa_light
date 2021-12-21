from django.db import models


class News(models.Model):
    published_date = models.DateField(verbose_name='Дата публикации')
    title = models.CharField(max_length=255,
                             verbose_name='Заголовок публикации')
    content = models.TextField(verbose_name='Контент', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
