from django.db import models
# For ordering news articles by date
from django.db.models import DateTimeField
from django.db.models.functions import Trunc

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.CharField(max_length=400)
    # gets rid of time stamp on entry
    # def date_published(self):
    #     return self.pub_date.strftime('%B %d %Y')

