# Generated by Django 2.0.3 on 2018-09-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_interest'),
        ('authentication', '0002_auto_20180621_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(to='project.Interest'),
        ),
    ]
