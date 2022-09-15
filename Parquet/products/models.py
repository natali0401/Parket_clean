from django.db import models

class Massiv(models.Model):
    name = models.CharField(max_length=255,verbose_name = 'Название')
    sort = models.CharField(max_length=255, verbose_name = 'Сорт')
    poroda = models.CharField(max_length=255, verbose_name = 'Порода')
    opis = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Паркет массив'
        verbose_name_plural = 'Паркет массив'

class Shpon(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    poroda = models.CharField(max_length=255, verbose_name='Порода')
    thickness = models.IntegerField(verbose_name='Толщина')
    opis = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шпон'
        verbose_name_plural = 'Шпон'


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ваше имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def str(self):
        return self.first_name

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"

