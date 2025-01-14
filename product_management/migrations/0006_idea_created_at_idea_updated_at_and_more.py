# Generated by Django 4.2.2 on 2023-09-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0005_delete_challengelisting"),
    ]

    operations = [
        migrations.AddField(
            model_name="idea",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="idea",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="idea",
            name="vote_count",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
