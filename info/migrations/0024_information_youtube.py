# Generated by Django 4.1.4 on 2022-12-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0023_remove_message_recaptcha"),
    ]

    operations = [
        migrations.AddField(
            model_name="information",
            name="youtube",
            field=models.URLField(blank=True, null=True),
        ),
    ]
