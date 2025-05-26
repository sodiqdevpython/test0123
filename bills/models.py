from django.db import models
from autoslug import AutoSlugField


class Bill(models.Model):
    """Model representing a bill with various details and payment status."""

    slug = AutoSlugField(unique=True, populate_from='date')
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Dana (masalan, 2024/11/22)'
    )
    institution_name = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )
    phone_number = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text='Tashkilotning telefon raqami'
    )
    email = models.EmailField(
        blank=True,
        null=True,
        help_text='Tashkilotning elektron pochta manzili'
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Tashkilot manzili'
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ko'proq ma'lumotlar"
    )
    payment_details = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="To'lov tafsilotlari"
    )
    amount = models.FloatField(
        verbose_name='Jami qarz miqdori',
        help_text="To'lanishi kerak bo'lgan umumiy miqdor"
    )
    status = models.BooleanField(
        default=False,
        verbose_name="To'langan",
        help_text="To'lov holati"
    )

    def __str__(self):
        return self.institution_name
