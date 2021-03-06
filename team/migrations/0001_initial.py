# Generated by Django 2.0.2 on 2018-03-12 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(choices=[(1, 'Freshman'), (2, 'Sophomore'), (3, 'Junior'), (4, 'Senior'), (5, 'Graduate')], default=1)),
                ('major_1', models.CharField(blank=True, default='', max_length=50)),
                ('major_2', models.CharField(blank=True, default='', max_length=50)),
                ('minor_1', models.CharField(blank=True, default='', max_length=50)),
                ('minor_2', models.CharField(blank=True, default='', max_length=50)),
                ('hometown', models.CharField(blank=True, default='', max_length=50)),
                ('team', models.CharField(choices=[('Rec', 'Rec'), ('Comp', 'Comp')], default='Rec', max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-year'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('member_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='team.Member')),
                ('position', models.CharField(blank=True, default='', max_length=50)),
            ],
            options={
                'ordering': ['position'],
                'abstract': False,
            },
            bases=('team.member',),
        ),
    ]
