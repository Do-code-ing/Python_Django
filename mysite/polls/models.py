from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 질문
    pub_date = models.DateTimeField("date published")  # 게시 날짜


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  # 선택 텍스트
    votes = models.IntegerField(default=0)  # 투표 집계
