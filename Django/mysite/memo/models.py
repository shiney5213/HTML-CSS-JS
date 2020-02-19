from django.db import models
from django.utils import timezone

class Memo(models.Model):

    author = models.ForeignKey('auth.User', 
                                on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True,
                                        null = True)
    cnt = models.IntegerField(default = 0)
    image = models.CharField(max_length = 200, null = True, blank = True)

    category = models.CharField(max_length = 10, default = 'common')

    def __str__(self):
        return self.title                                