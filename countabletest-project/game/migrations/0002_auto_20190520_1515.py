# Generated by Django 2.0.2 on 2019-05-20 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image01',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='game',
            name='phrase01',
            field=models.TextField(null=True),
        ),
    ]