# Generated by Django 2.2 on 2021-02-12 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harbor_international_app', '0003_auto_20210211_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
