# Generated by Django 3.1.2 on 2020-12-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0002_auto_20201211_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='Z0S19M9UPOPH8FWFWJTR', max_length=20),
        ),
    ]