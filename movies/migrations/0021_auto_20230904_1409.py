# Generated by Django 3.2.7 on 2023-09-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_auto_20230902_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='highlightEnd',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='highlightStart',
        ),
        migrations.AddField(
            model_name='episode',
            name='highlights',
            field=models.JSONField(blank=True, null=True),
        ),
    ]