# Generated by Django 4.2.7 on 2024-07-07 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0007_greeninitiativecomment_personal_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
    ]
