# Generated by Django 5.0 on 2023-12-13 16:32

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_contacts', '0006_alter_contact_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
        migrations.CreateModel(
            name='PhoneEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_contacts.contact')),
            ],
        ),
    ]
