# Generated by Django 4.2.2 on 2023-08-25 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("talent", "0008_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="bountyclaim",
            name="expected_finish_date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
