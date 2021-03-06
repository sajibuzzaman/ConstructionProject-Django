# Generated by Django 3.1.3 on 2021-03-23 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConstructionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='category/')),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=20)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConstructionProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='product/')),
                ('new_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amount', models.IntegerField(default=0)),
                ('min_amount', models.IntegerField(default=3)),
                ('detail', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=20)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConstructApp.constructioncategory')),
            ],
        ),
    ]
