# Generated by Django 3.1 on 2020-09-12 09:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200912_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 9, 58, 12, 870824, tzinfo=utc), verbose_name='date_listed'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 9, 58, 12, 872264, tzinfo=utc)),
        ),
    ]
