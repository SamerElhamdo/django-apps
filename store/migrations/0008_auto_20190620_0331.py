# Generated by Django 2.2.2 on 2019-06-20 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20190620_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='category',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='attr',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color')], default='size', max_length=150),
        ),
    ]
