# Generated by Django 2.2 on 2021-02-18 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harbor_international_app', '0004_auto_20210211_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algebra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=3000)),
                ('videofile', models.FileField(null=True, upload_to='algebra/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=3000)),
                ('videofile', models.FileField(null=True, upload_to='geometry/', verbose_name='')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='caption',
        ),
    ]
