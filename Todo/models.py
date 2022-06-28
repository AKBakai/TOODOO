from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=255, verbose_name='Текст')
    complete = models.BooleanField(default=False)                   


    def __str__(self) -> str:
        return f'ID: {self.id} Text: {self.text}'
        
