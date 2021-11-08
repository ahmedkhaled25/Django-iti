# Generated by Django 3.2.9 on 2021-11-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Movie Name')),
                ('description', models.TextField(verbose_name='Movie Description')),
                ('likes', models.IntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('Production_date', models.DateTimeField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
