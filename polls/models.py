from django.db import models

class Question(models.Model): # models store class Model
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True) #will create question at the time submitting questions

    def __str__(self):
        return f'Question: {self.question_text}'
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'Question #: {self.question.id}, Answer: {self.choice_text}'


