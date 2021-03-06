# Generated by Django 3.0.6 on 2020-05-20 10:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0002_auto_20200520_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, help_text='Select team members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='secrets',
            field=models.ManyToManyField(blank=True, help_text='Select team secrets', to='storage.Secret'),
        ),
    ]
