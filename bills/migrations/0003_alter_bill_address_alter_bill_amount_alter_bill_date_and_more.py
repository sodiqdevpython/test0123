# Generated by Django 5.1 on 2025-05-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_alter_bill_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='address',
            field=models.CharField(blank=True, help_text='Tashkilot manzili', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.FloatField(help_text="To'lanishi kerak bo'lgan umumiy miqdor", verbose_name='Jami qarz miqdori'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Dana (masalan, 2024/11/22)'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='description',
            field=models.CharField(blank=True, help_text="Ko'proq ma'lumotlar", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='email',
            field=models.EmailField(blank=True, help_text='Tashkilotning elektron pochta manzili', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='payment_details',
            field=models.CharField(help_text="To'lov tafsilotlari", max_length=255),
        ),
        migrations.AlterField(
            model_name='bill',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, help_text='Tashkilotning telefon raqami', null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='status',
            field=models.BooleanField(default=False, help_text="To'lov holati", verbose_name="To'langan"),
        ),
    ]
