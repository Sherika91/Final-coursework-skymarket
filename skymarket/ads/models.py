from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Ad(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField(**NULLABLE,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads_author')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_author')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments_ad')
    description = models.TextField(**NULLABLE,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
