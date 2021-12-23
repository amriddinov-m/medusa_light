from django.db import models


class News(models.Model):
    date = models.DateField(verbose_name='Дата публикации')
    subject = models.CharField(max_length=255,
                               verbose_name='Заголовок публикации')
    content = models.TextField(verbose_name='Контент', blank=True, null=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
