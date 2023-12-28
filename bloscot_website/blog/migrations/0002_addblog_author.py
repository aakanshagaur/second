# Generated by Django 4.2.6 on 2023-12-20 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="addblog",
            name="author",
            field=models.ForeignKey(
                default=" ",
                on_delete=django.db.models.deletion.CASCADE,
                to="users.adduser",
            ),
            preserve_default=False,
        ),
    ]
