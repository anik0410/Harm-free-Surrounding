# Generated by Django 5.1.3 on 2024-11-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0014_complaint_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greeninitiativecomment',
            name='green_initiative',
        ),
        migrations.RemoveField(
            model_name='greeninitiativecomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='area',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='pincode',
        ),
        migrations.AddField(
            model_name='complaint',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='GreenInitiative',
        ),
        migrations.DeleteModel(
            name='GreenInitiativeComment',
        ),
    ]
