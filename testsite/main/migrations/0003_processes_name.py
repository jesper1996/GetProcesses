# Generated by Django 4.0.4 on 2022-05-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_processes_alter_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='processes',
            name='name',
            field=models.CharField(default='test', max_length=5000),
        ),
    ]