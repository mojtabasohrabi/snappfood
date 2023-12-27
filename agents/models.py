from django.db import models


class Agent(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='نام پشتیبان'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان شروع همکاری"
    )

    def __str__(self):
        return self.name