# Generated by Django 4.0.2 on 2022-03-24 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_lab_material_sec_lab_material_lab_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='assisstant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.assisstant'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.assisstant'),
        ),
    ]
