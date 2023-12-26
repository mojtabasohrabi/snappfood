from django.db import models


class Vendor(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='نام فروشگاه'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="زمان شروع همکاری"
    )
