# Generated by Django 4.2.2 on 2023-06-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_signup_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='initials',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='signup',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]