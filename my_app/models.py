from django.db import models

# Create your models here.
class TestModel(models.Model):
    string = models.CharField(max_length=20, verbose_name="Название поля 1")
    date = models.DateField(verbose_name="Дата")
    datetime = models.DateTimeField(verbose_name="Дата и время")
    checkbox_yes = models.BooleanField(verbose_name="Да")
    checkbox_no = models.BooleanField(verbose_name="Нет")

    integer = models.IntegerField(verbose_name="Число")
    choices = models.IntegerField(verbose_name="Выборка", choices=(
        (1, "one"),
        (2, "two"),
        (3, "three"),
    ))
    text_box = models.TextField(verbose_name="Ваши жалобы", blank=True, null=True) # null - позволяет БД добавить пустым text_box, blank - позволяет в форме  админке добавить пустым
    def __str__(self):
        return f"Тестовая Модель № {self.id} "