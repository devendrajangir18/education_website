# Generated by Django 4.0.1 on 2022-10-19 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_logout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='email',
        ),
        migrations.RemoveField(
            model_name='login',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
    ]
