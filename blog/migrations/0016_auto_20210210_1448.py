# Generated by Django 3.1.4 on 2021-02-10 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentlar', to='blog.post', verbose_name='commentlar'),
        ),
    ]
