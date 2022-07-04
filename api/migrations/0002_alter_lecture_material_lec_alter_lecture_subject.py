# Generated by Django 4.0.5 on 2022-07-04 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='material_lec',
            field=models.FileField(upload_to='material/lecture/'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_lecture', to='api.subject'),
        ),
    ]
