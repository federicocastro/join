# Generated by Django 2.0.3 on 2018-06-21 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gallery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extended', to='photologue.Gallery'),
        ),
    ]
