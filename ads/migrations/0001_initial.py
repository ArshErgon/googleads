# Generated by Django 3.0.5 on 2020-04-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_title', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('recipe', models.TextField()),
            ],
        ),
    ]
