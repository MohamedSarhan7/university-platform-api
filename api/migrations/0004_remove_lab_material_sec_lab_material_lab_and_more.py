# Generated by Django 4.0.2 on 2022-03-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_assisstant_section_subject_assisstant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='material_sec',
        ),
        migrations.AddField(
            model_name='lab',
            name='material_lab',
            field=models.FileField(blank=True, null=True, upload_to='uploads/material/section'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='material_lec',
            field=models.FileField(blank=True, null=True, upload_to='uploads/material/lecture'),
        ),
        migrations.DeleteModel(
            name='Matiral_Lab',
        ),
        migrations.DeleteModel(
            name='Matiral_Lec',
        ),
    ]
