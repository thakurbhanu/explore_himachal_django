# Generated by Django 3.2.4 on 2021-06-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placename', models.CharField(default='#', max_length=200)),
                ('placeimage', models.CharField(blank=True, default='#', max_length=5000, null=True)),
                ('placetagline', models.CharField(default='#', max_length=200)),
                ('placedescription1', models.TextField(blank=True, default='#', max_length=5000, null=True)),
                ('placedescription2', models.TextField(blank=True, default='#', max_length=5000, null=True)),
                ('placegooglemap', models.CharField(blank=True, default='#', max_length=200, null=True)),
            ],
        ),
    ]
