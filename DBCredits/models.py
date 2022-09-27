from django.db import models

# Create your models here.


class Users(models.Model):

    login = models.CharField('login', max_length=255)
    registration_date = models.DateField('registration_date')

    def __srt__(self):
        return self.login


class Dictionary(models.Model):

    name = models.CharField('name', max_length=255)

    def __srt__(self):
        return self.name


class Plans(models.Model):

    period = models.DateField('period')
    sum = models.IntegerField('sum')
    category_id = models.ForeignKey(Dictionary, on_delete=models.CASCADE)

    def __srt__(self):
        return self.period


class Credits(models.Model):

    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    issuance_date = models.DateField('issuance_date')
    return_date = models.DateField('return_date')
    actual_return_date = models.DateField('actual_return_date')
    body = models.IntegerField('body')
    percent = models.FloatField('percent')

    def __srt__(self):
        return self.issuance_date


class Payments(models.Model):

    credit_id = models.ForeignKey(Credits, on_delete=models.CASCADE)
    payment_date = models.DateField('payment_date')
    type_id = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    sum = models.FloatField('sum')

    def __srt__(self):
        return self.payment_date

