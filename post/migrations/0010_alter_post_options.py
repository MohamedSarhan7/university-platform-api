# Generated by Django 4.0.5 on 2022-07-21 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_rename_date_post_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
    ]
