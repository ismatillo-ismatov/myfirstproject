# Generated by Django 3.1.4 on 2021-02-06 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210131_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': "User ma'lumot", 'verbose_name_plural': "User ma'lumotlari"},
        ),
        migrations.AlterModelOptions(
            name='userdata',
            options={},
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='blog.userdata', verbose_name='Avtor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='commentlar'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='blog.Tag', verbose_name='Foydali teglar'),
        ),
    ]