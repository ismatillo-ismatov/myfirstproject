# Generated by Django 3.1.4 on 2021-02-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210210_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=17)),
                ('surname', models.CharField(max_length=20)),
                ('msg', models.TextField()),
                ('phone', models.CharField(max_length=25)),
            ],
        ),
    ]
