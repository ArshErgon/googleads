# Generated by Django 3.0.5 on 2020-05-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20200501_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='slug_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
