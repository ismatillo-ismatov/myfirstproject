# Generated by Django 3.1.4 on 2021-03-02 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20210221_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='like_dislike',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
