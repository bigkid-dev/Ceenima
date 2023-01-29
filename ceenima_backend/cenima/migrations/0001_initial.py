# Generated by Django 4.1.4 on 2022-12-14 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('summary', models.CharField(max_length=50)),
                ('link', models.TextField()),
                ('image_link', models.TextField()),
                ('time_showing', models.TimeField()),
                ('second_time_showing', models.TimeField()),
                ('third_time_showinng', models.TimeField()),
                ('fourth_time_showing', models.TimeField()),
            ],
        ),
    ]