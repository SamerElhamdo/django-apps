# Generated by Django 2.2.2 on 2019-06-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='color',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='category',
            field=models.CharField(choices=[('color', 'اللون'), ('size', 'القياس')], default='size', max_length=150),
        ),
    ]