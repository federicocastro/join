# Generated by Django 2.0.3 on 2018-10-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20181025_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='youtube_profile',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]