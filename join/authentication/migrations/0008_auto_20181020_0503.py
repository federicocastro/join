# Generated by Django 2.0.3 on 2018-10-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20181018_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook_profile',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gplus_profile',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_profile',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin_profile',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_profile',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
