# Generated by Django 5.1.3 on 2024-11-20 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0013_complaint_voted_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/complaint_videos/'),
        ),
    ]
