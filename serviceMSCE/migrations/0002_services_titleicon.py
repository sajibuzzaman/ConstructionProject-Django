# Generated by Django 3.1.3 on 2021-03-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceMSCE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='titleicon',
            field=models.CharField(default='sajib', max_length=200),
            preserve_default=False,
        ),
    ]
