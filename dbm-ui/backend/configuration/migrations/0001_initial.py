# Generated by Django 3.2.4 on 2023-04-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IPWhitelist",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("creator", models.CharField(max_length=64, verbose_name="创建人")),
                ("create_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("updater", models.CharField(max_length=64, verbose_name="修改人")),
                ("update_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
                ("bk_biz_id", models.IntegerField(verbose_name="业务ID")),
                ("remark", models.CharField(max_length=255, verbose_name="备注")),
                ("ips", models.JSONField(verbose_name="ip列表")),
            ],
            options={
                "verbose_name": "IP白名单",
                "verbose_name_plural": "IP白名单",
            },
        ),
        migrations.CreateModel(
            name="PasswordPolicy",
            fields=[
                (
                    "account_type",
                    models.CharField(
                        choices=[
                            ("mysql", "MySQL"),
                            ("redis", "Redis"),
                            ("kafka", "Kafka"),
                            ("hdfs", "HDFS"),
                            ("es", "ElasticSearch"),
                            ("pulsar", "Pulsar"),
                            ("influxdb", "InfluxDB"),
                            ("cloud", "Cloud"),
                        ],
                        max_length=32,
                        primary_key=True,
                        serialize=False,
                        verbose_name="账号类型",
                    ),
                ),
                ("policy", models.JSONField(verbose_name="密码安全策略")),
            ],
            options={
                "verbose_name": "密码安全策略",
            },
        ),
        migrations.CreateModel(
            name="SystemSettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("creator", models.CharField(max_length=64, verbose_name="创建人")),
                ("create_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("updater", models.CharField(max_length=64, verbose_name="修改人")),
                ("update_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
                ("type", models.CharField(max_length=64, verbose_name="类型")),
                ("key", models.CharField(max_length=64, unique=True, verbose_name="关键字唯一标识")),
                ("value", models.JSONField(verbose_name="系统设置值")),
                ("desc", models.CharField(max_length=255, verbose_name="描述")),
            ],
            options={
                "verbose_name": "系统设置",
                "verbose_name_plural": "系统设置",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=128, verbose_name="用户名")),
                ("label", models.CharField(max_length=32, verbose_name="标签")),
                ("values", models.JSONField(verbose_name="配置值")),
            ],
            options={
                "unique_together": {("username", "label")},
            },
        ),
        migrations.CreateModel(
            name="DBAdministrator",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("bk_biz_id", models.IntegerField(verbose_name="业务ID")),
                (
                    "db_type",
                    models.CharField(
                        choices=[
                            ("mysql", "MySQL"),
                            ("redis", "Redis"),
                            ("kafka", "Kafka"),
                            ("hdfs", "HDFS"),
                            ("es", "ElasticSearch"),
                            ("pulsar", "Pulsar"),
                            ("influxdb", "InfluxDB"),
                            ("cloud", "Cloud"),
                        ],
                        max_length=32,
                        verbose_name="数据库类型",
                    ),
                ),
                ("users", models.JSONField(verbose_name="人员列表")),
            ],
            options={
                "verbose_name": "DBA人员设置",
                "verbose_name_plural": "DBA人员设置",
                "unique_together": {("bk_biz_id", "db_type")},
            },
        ),
    ]
