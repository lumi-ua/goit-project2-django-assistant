# Generated by Django 5.0 on 2023-12-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]