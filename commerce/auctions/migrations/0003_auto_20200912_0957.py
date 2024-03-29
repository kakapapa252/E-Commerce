# Generated by Django 3.1 on 2020-09-12 09:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20200912_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 9, 57, 8, 749500, tzinfo=utc), verbose_name='date_listed'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/default.png', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 9, 57, 8, 750698, tzinfo=utc)),
        ),
    ]
