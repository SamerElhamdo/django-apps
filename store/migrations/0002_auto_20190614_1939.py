# Generated by Django 2.2.2 on 2019-06-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodect',
            name='discount',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='new_price',
            field=models.IntegerField(blank=True),
        ),
    ]