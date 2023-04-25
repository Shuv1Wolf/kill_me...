from django.db import models

# Create your models here.
# старые тестовые модели
class paymentModel1(models.Model):
    field = models.DecimalField(decimal_places=False, max_digits=100, blank=True)


class paymentModel2(models.Model):
    field = models.DecimalField(decimal_places=False, max_digits=100, blank=True)


class paymentModel3(models.Model):
    field = models.DecimalField(decimal_places=False, max_digits=100, blank=True)


# релизная модель
class paymentModelAll(models.Model):
    field1 = models.DecimalField(decimal_places=False, max_digits=100, blank=True)
    field2 = models.DecimalField(decimal_places=False, max_digits=100, blank=True)
    field3 = models.DecimalField(decimal_places=False, max_digits=100, blank=True)