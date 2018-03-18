# Generated by Django 2.0 on 2018-03-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, unique=True, verbose_name='主机名')),
                ('network_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='外网IP')),
                ('inner_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否运行')),
                ('system', models.CharField(blank=True, max_length=128, null=True, verbose_name='系统版本')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存')),
                ('disk', models.CharField(blank=True, max_length=256, null=True, verbose_name='硬盘')),
                ('bandwidth', models.IntegerField(blank=True, default='1', null=True, verbose_name='带宽')),
                ('platform', models.CharField(choices=[('阿里云', '阿里云'), ('AWS', 'AWS'), ('其他', '其他')], max_length=128, verbose_name='平台')),
                ('Instance_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='实例ID')),
                ('region', models.CharField(blank=True, max_length=256, null=True, verbose_name='地区')),
                ('manager', models.CharField(choices=[('何全', '何全'), ('其他', '其他')], max_length=128, verbose_name='负责人')),
                ('ctime', models.DateTimeField(verbose_name='购买时间')),
                ('utime', models.DateTimeField(verbose_name='到期时间')),
                ('ps', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '资产管理',
                'verbose_name_plural': '资产管理',
                'db_table': 'asset',
                'permissions': {('read_asset', '只读资产管理')},
            },
        ),
    ]