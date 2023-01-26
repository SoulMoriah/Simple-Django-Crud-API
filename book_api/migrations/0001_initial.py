# Generated by Django 4.1.1 on 2023-01-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('number_of_pages', models.IntegerField()),
                ('publish_date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
