from django.db import models
# For ordering news articles by date
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField()
    # gets rid of time stamp on entry
    # def date_published(self):
    #     return self.pub_date.strftime('%B %d %Y')
