# Generated by Django 2.1.5 on 2019-02-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190220_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='workplace',
            field=models.CharField(max_length=50, verbose_name='지점'),
        ),
    ]
