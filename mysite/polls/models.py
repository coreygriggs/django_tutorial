from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(modes.Model):
    question = models.ForeignKey(Question)
    choice_text = modeslCharField(max_length=200)
    votes = models.IntegerField(default=0)