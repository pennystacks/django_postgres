# Generated by Django 4.1.4 on 2022-12-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_postgres", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="benchmarkuser",
            name="is_admin",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
