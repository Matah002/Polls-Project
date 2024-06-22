from django.db import models
import datetime 
from django.utils import timezone
from django.contrib import admin

# Here we define our database
# In case you change anything in this file "models.py", you  have to run "python manage.py migrate" to make migrations

# The would have the following if written in SQL

# CREATE TABLE Question (
#     id INTEGER PRIMARY KEY,
#     question_text VARCHAR(200) NOT NULL,
#     pub_date DATETIME NOT NULL
# );

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    @admin.display(
         boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now # <<< code to calculate present time

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    