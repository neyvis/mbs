# Generated by Django 2.2.12 on 2020-05-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_bs_app', '0004_auto_20200421_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
