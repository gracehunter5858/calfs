# Generated by Django 2.0.2 on 2018-03-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_event_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='display_on_site',
            field=models.BooleanField(default=True),
        ),
    ]
