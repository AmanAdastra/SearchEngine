# Generated by Django 4.0.3 on 2022-03-31 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='object_id',
            field=models.TextField(),
        ),
    ]
