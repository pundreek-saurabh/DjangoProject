import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    question_text = models.CharField(max_length=200,default=False)

    def was_published_recently(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text