# Generated by Django 3.1.3 on 2020-11-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
