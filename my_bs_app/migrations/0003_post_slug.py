# Generated by Django 2.2.12 on 2020-04-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_bs_app', '0002_auto_20200418_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
