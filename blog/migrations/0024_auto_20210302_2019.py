# Generated by Django 3.1.4 on 2021-03-02 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_userdata_like_dislike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='blog.userdata', verbose_name='category'),
        ),
    ]