# Generated by Django 4.1.4 on 2022-12-31 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cenima', '0003_alter_shows_fourth_time_showing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cenima_Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('summary', models.CharField(max_length=50)),
                ('link', models.TextField(max_length=200)),
                ('location', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_link', models.TextField(max_length=200)),
                ('time_showing', models.TimeField()),
                ('second_time_showing', models.TimeField()),
                ('third_time_showing', models.TimeField()),
                ('fourth_time_showing', models.TimeField()),
                ('date_showing', models.DateTimeField()),
                ('second_date_showing', models.DateTimeField()),
                ('third_date_showing', models.DateTimeField()),
                ('fourth_date_showing', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='New_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_pic', models.ImageField(blank=True, upload_to='new_movies_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Upcoming_Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upcoming_pic', models.ImageField(blank=True, upload_to='upcoming_movie_img')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_name', models.CharField(max_length=50)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tickets_quantity', models.IntegerField()),
                ('location', models.TextField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
