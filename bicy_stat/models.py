from django.db import models

# Create your models here.
class Bicy_stats(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    content = models.TextField('Content', null=True)
    period = models.DateTimeField('Period')

    class Meta:
        verbose_name = 'stat'
        verbose_name_plural = 'stats'
        ordering = ('-period',)

    def __str__(self):
        return self.title