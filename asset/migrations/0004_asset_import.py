# Generated by Django 2.0.3 on 2018-03-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20180318_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='asset_import',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='assets/%Y%m%d74514', verbose_name='文件')),
            ],
        ),
    ]