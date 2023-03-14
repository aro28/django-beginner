from django.contrib import admin

# Register your models here.
from .models import Question, Choice
# admin.site.register(Question)
# admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
admin.site.register(Question, QuestionAdmin) # to register


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes']
    search_fields = ['choice_text', 'question__question_text']