# Generated by Django 3.1.4 on 2020-12-04 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('details', models.TextField(max_length=250, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='Post')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.category')),
            ],
        ),
    ]