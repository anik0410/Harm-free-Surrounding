# Generated by Django 5.1.3 on 2024-11-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0011_delete_employee_delete_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaint',
            name='thumbs_up',
            field=models.PositiveIntegerField(default=0),
        ),
    ]