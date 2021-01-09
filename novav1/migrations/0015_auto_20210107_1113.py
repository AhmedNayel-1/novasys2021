# Generated by Django 3.1.2 on 2021-01-07 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0014_auto_20210107_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='6GXGOCI9PGRR95ZDGMI8', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Area',
            field=models.ForeignKey(blank=True, db_column='Area', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Area', to='novav1.area'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ComeFrom',
            field=models.ForeignKey(blank=True, db_column='Id_ComeFrom', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='novav1.comefrom'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Gender',
            field=models.ForeignKey(blank=True, db_column='Id_Gender', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='novav1.gender'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='JopArea',
            field=models.ForeignKey(blank=True, db_column='JopArea', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='JopArea', to='novav1.area'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='PatientFfriend',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, db_column='Id_Doctor', db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='novav1.doctorout'),
        ),
    ]
