# Generated by Django 2.0.7 on 2018-07-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zufang', '0012_zufang_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='zufang_content_info',
            name='city_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='zufang_content_info',
            name='img',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='zufang_content_info',
            name='mianji',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='zufang_content_info',
            name='month_money',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='zufang_content_info',
            name='next_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='zufang_content_info',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='zufang_content_info',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='zufang_content_info',
            name='jjr',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='zufang_content_info',
            name='jjr_img',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='zufang_content_info',
            name='jjr_phone',
            field=models.CharField(default='', max_length=200),
        ),
    ]