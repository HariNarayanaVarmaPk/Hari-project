# Generated by Django 5.0.2 on 2024-03-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cinema",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default="2024-03-01 12:23"),
            preserve_default=False,
        ),
    ]
