from django.db import models

# Create your models here.
class toDoList(models.Model):
    name = models.CharField(max_Length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.Foreignkey
