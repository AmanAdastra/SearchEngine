# Generated by Django 4.0.3 on 2022-03-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_rename_color_car_category_alter_car_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(),
        ),
    ]