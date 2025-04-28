from django.db import models


class FormData(models.Model):

    data = models.JSONField(
        verbose_name="Данные формы", help_text="Массив значений динамических полей"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"FormData #{self.id} ({self.created_at})"
