# Generated by Django 3.1.2 on 2021-01-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0015_auto_20210107_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='5HI2OZ1MMPGHY4ABQ1FF', max_length=20),
        ),
    ]