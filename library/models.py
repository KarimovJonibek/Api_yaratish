from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'books'
        verbose_name_plural = 'books'
