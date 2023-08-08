# Generated by Django 4.2.3 on 2023-08-08 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='purchase_date',
            field=models.DateField(default=datetime.date(2023, 8, 1), verbose_name='Purchased Date'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=(5, '5'), max_length=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Review Date'),
        ),
    ]
