# Generated by Django 4.0.4 on 2022-05-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_processes_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='processes',
            name='for_delete',
            field=models.CharField(default='test', max_length=5000),
        ),
    ]
