# Generated by Django 2.2.7 on 2019-11-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0003_auto_20191121_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesreport',
            name='store',
            field=models.CharField(default='none', max_length=128),
        ),
    ]
