from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Чернетка'
        PUBLISHED = 'PB', 'Підтверджено'

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name='Автор'
    )
    pidrozdil = models.CharField(max_length=250, verbose_name='Підрозділ')
    marshrut = models.CharField(max_length=250, verbose_name='Маршрут')
    sostav = models.TextField(verbose_name='Склад в/с')
    data_viezd = models.DateField(verbose_name='Дата виїзду')
    time_viezd = models.TimeField(default=timezone.now, verbose_name='Час виїзду')
    time_back = models.TimeField(default=timezone.now, verbose_name='Час повернення')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Публікація')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.PUBLISHED,
        verbose_name='Статус'
    )

    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering=['-publish']
        indexes =[
            models.Index(fields=['-publish']),
        ]
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.pidrozdil