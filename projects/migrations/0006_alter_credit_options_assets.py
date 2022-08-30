# Generated by Django 4.1 on 2022-08-26 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_options_alter_project_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credit',
            options={'ordering': ('-rank', 'role', 'pk')},
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.TextField(blank=True)),
                ('rank', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'ordering': ('-rank', 'caption', 'pk'),
            },
        ),
    ]