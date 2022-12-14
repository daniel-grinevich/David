# Generated by Django 4.1 on 2022-08-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('feature_image', models.ImageField(upload_to='')),
                ('rank', models.IntegerField(default=0)),
                ('is_in_navigation', models.BooleanField(default=True)),
                ('navigation_title', models.CharField(max_length=30)),
            ],
        ),
    ]
