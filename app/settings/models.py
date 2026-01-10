from django.db import models
from ckeditor.fields import RichTextField


class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголвок',
        blank=True, null=True
    )
    descritpion = RichTextField(
        verbose_name='Текст',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото',
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'    