import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 질문
    pub_date = models.DateTimeField("date published")  # 게시 날짜

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  # 선택 텍스트
    votes = models.IntegerField(default=0)  # 투표 집계

    def __str__(self):
        return self.choice_text
