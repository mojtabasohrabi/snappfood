from django.db import models
from vendors.models import Vendor
from agents.models import Agent


class Order(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        related_name='vendor',
        verbose_name='فروشگاه',
        on_delete=models.CASCADE,
    )

    delivery_time = models.PositiveIntegerField(
        verbose_name='زمان آماده سازی'
    )

    delay = models.PositiveIntegerField(
        verbose_name='میزان تاخیر این سفارش',
        default=0
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ثبت سفارش"
    )

    updated = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان تغییر سفارش"
    )

    sent = models.BooleanField(
        default=False,
        verbose_name='وضعیت ارسال سفارش'
    )

    @property
    def delivery_time_by_delay(self):
        return self.delay + self.delivery_time

    def __str__(self):
        return f" سفارش شماره{self.id}:  از فروشگاه:{self.vendor.name}"


class Trip(models.Model):
    order = models.OneToOneField(
        to=Order,
        on_delete=models.PROTECT,
        related_name='google_credentials',
    )

    TRIP_STATUS = (
        ("DELIVERED", "سفارش به مقصد رسیده"),
        ("PICKED", "دریافت سفارش"),
        ("AT_VENDOR", "در فروشگاه"),
        ("ASSIGNED", "پیک در راه فروشگاه")
    )

    status = models.CharField(
        verbose_name="وضعیت سفر",
        choices=TRIP_STATUS,
        default='ASSIGNED',
        max_length=50
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ثبت سفر"
    )


class DelayReport(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='order',
        verbose_name='سفارش مربوط به این گزارش',
        on_delete=models.CASCADE,
    )

    agent = models.ForeignKey(
        Agent,
        related_name='agent',
        verbose_name='پشتیبان بررسی کننده این گزارش',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    DELAY_STATUS = (
        ("NEW_DELIVERY_TIME", "زمان آماده سازی جدید ارائه شده"),
        ("WAIT_FOR_AGENT", "منتظر انتخاب پشتیبان"),
        ("IN_PROGRESS", "در حال بررسی"),
        ("FINISHED", "به پایان رسیده")
    )

    status = models.CharField(
        verbose_name="وضعیت گزارش",
        choices=DELAY_STATUS,
        default='WAIT_FOR_AGENT',
        max_length=50
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ثبت گزارش"
    )
