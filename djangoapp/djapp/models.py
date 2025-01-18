from django.db import models

class SalaryData(models.Model):
    year = models.IntegerField(unique=True, verbose_name="Год")
    average_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Средняя зарплата")

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Данные о зарплате"
        verbose_name_plural = "Данные о зарплатах"
        ordering = ['-year']