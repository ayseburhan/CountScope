# Generated by Django 5.0 on 2023-12-30 14:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("countscope", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="countscope",
            name="imageUrl",
        ),
        migrations.RemoveField(
            model_name="countscope",
            name="isActive",
        ),
    ]
