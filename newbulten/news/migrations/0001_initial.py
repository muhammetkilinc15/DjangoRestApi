# Generated by Django 5.0.6 on 2024-06-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('city', models.CharField(max_length=120)),
                ('published_date', models.DateField()),
                ('isActive', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
