# Generated by Django 3.2.8 on 2021-10-19 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='publish_date',
            new_name='pub_date',
        ),
    ]
