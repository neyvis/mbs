# Generated by Django 2.2.12 on 2020-04-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_bs_app', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
