# Generated by Django 2.0.2 on 2018-03-12 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officer',
            name='member_ptr',
        ),
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.DeleteModel(
            name='Officer',
        ),
    ]
