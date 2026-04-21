from django.db import models

# Create your models here.
class Product(models.Model): #это создаёт таблицу в базе
  name = models.CharField(max_length=100) # Название товара (строка до 100 символов 
  description = models.TextField() # Описание товара (длинный текст)
  price = models.IntegerField()# Цена товара (целое число)
  created_at = models.DateTimeField(auto_now_add=True) # Дата создания (ставится автоматически)
  def __str__(self):# Как объект будет отображаться (например в админке)
    return self.name