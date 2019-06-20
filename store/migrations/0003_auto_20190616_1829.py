# Generated by Django 2.2.2 on 2019-06-16 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190614_1939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prodect',
            new_name='Product',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=10)),
                ('full_name', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=150)),
                ('accept', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
    ]