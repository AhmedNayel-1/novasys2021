# Generated by Django 3.1.2 on 2020-12-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0008_auto_20201215_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='XM2AIQ9WJTTFVEHZD770', max_length=20),
        ),
    ]