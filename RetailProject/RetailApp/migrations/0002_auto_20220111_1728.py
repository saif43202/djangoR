# Generated by Django 3.1.7 on 2022-01-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RetailApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]