# Generated by Django 4.0.5 on 2022-07-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='image',
            field=models.ImageField(blank=True, default='./images/users/default.jpg', null=True, upload_to='Profile-Pic/'),
        ),
    ]
