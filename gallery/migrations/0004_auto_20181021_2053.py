# Generated by Django 2.1.2 on 2018-10-22 03:53

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20181021_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
