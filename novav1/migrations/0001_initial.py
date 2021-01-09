# Generated by Django 3.1.2 on 2020-12-11 07:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AreaName', models.CharField(blank=True, db_column='Text_Area', max_length=150, null=True)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BranchName', models.CharField(default='', max_length=50)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clinc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClincName', models.CharField(max_length=50)),
                ('cereatedDate', models.DateField(auto_now_add=True, null=True)),
                ('Active', models.BooleanField(default=True)),
                ('StartDdate', models.DateField(auto_now_add=True, null=True)),
                ('CloseDdate', models.DateField(blank=True, null=True)),
                ('Branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Comefrom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComeFrom', models.CharField(blank=True, db_column='Text_ComeFrom', max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeviceName', models.CharField(max_length=50)),
                ('DeviceFunction', models.CharField(max_length=50)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocName', models.CharField(blank=True, db_column='DocNameIN', default='New Doctor', max_length=150, null=True)),
                ('DocSpecialty', models.CharField(blank=True, db_column='DocSpecialty', default='', max_length=150, null=True)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocName', models.CharField(blank=True, db_column='DocNameOut', default='New Doctor', max_length=150, null=True)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(blank=True, db_column='Gender_Text', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('CountBalces', models.FloatField(default=0)),
                ('BalcesNumber', models.FloatField(default=0)),
                ('description_short', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JopName', models.CharField(blank=True, db_column='Text_Jop', max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(default='YK2RINONX6NAD283G1YR', max_length=20)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('order_type', models.IntegerField(blank=True, choices=[(1, 'SALE'), (2, 'BALLS TRANSFER Add '), (3, 'BALLS TRANSFER reducing '), (4, 'PYMENT'), (5, 'Refunds')], default=1, null=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('TotalPrice', models.IntegerField(default=0)),
                ('Discount', models.IntegerField(default=0)),
                ('Net', models.IntegerField(blank=True, default=0, null=True)),
                ('Cash', models.IntegerField(default=0)),
                ('Remmaining', models.IntegerField(default=0)),
                ('Refunds', models.IntegerField(default=0)),
                ('balls', models.IntegerField(default=0)),
                ('ballsRemmaining', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=50)),
                ('Cash_efect', models.IntegerField(default=0)),
                ('Balls_efect', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientName', models.CharField(blank=True, db_column='FirstName', max_length=50, null=True)),
                ('PatientSecondName', models.CharField(blank=True, db_column='SecondName', max_length=50, null=True)),
                ('PatientThirdName', models.CharField(blank=True, db_column='ThirdName', max_length=50, null=True)),
                ('Active', models.BooleanField(default=True)),
                ('PatientCode', models.CharField(blank=True, db_column='Pationt_Code', max_length=50, null=True)),
                ('PatientBbarcode', models.CharField(blank=True, db_column='Pationt_BarCode', max_length=50, null=True)),
                ('Birtdate', models.DateField(blank=True, null=True)),
                ('PlaceJop', models.CharField(blank=True, db_column='Place_Jop', max_length=150, null=True)),
                ('PatientMobile1', models.IntegerField(blank=True, null=True)),
                ('PatientMobile2', models.IntegerField(blank=True, null=True)),
                ('BallceBalance', models.IntegerField(default=0)),
                ('UsedBalls', models.IntegerField(default=0)),
                ('RemmainingBalance', models.IntegerField(default=0)),
                ('AmountBalance', models.IntegerField(default=0)),
                ('paid', models.IntegerField(default=0)),
                ('Remmainingamount', models.IntegerField(default=0)),
                ('Area', models.ForeignKey(blank=True, db_column='Area', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Area', to='novav1.area')),
                ('ComeFrom', models.ForeignKey(blank=True, db_column='Id_ComeFrom', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='novav1.comefrom')),
                ('Gender', models.ForeignKey(blank=True, db_column='Id_Gender', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='novav1.gender')),
                ('Jop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.jop')),
                ('JopArea', models.ForeignKey(blank=True, db_column='JopArea', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='JopArea', to='novav1.area')),
                ('PatientFfriend', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.patient')),
                ('doctor', models.ForeignKey(blank=True, db_column='Id_Doctor', default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='novav1.doctorout')),
            ],
        ),
        migrations.CreateModel(
            name='pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BodyPart', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('BallsNumber', models.IntegerField(default=0)),
                ('time_of_part', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stractuer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StractuerPer', models.IntegerField(blank=True, db_column='Id_Stractuer_Per', null=True)),
                ('NameStractuer', models.IntegerField(blank=True, db_column='Name_Stractuer', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=100)),
                ('success', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='novav1.patient')),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='novav1.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomName', models.CharField(max_length=50)),
                ('RoomActive', models.BooleanField(default=True)),
                ('Branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.branch', verbose_name='Branch Name')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateReservation', models.DateTimeField(auto_now_add=True, null=True)),
                ('FromTimeReservation', models.DateTimeField(blank=True, db_column='FromTime_Reservation', null=True)),
                ('ToTimeReservation', models.DateTimeField(blank=True, db_column='ToTime_Reservation', null=True)),
                ('Reservation', models.CharField(blank=True, db_column='Text_Reservation', max_length=350, null=True)),
                ('balance', models.FloatField()),
                ('Branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.branch')),
                ('Clinc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.clinc')),
                ('Doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.doctorin')),
                ('Patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novav1.order')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PackageName', models.CharField(max_length=50)),
                ('PackageNewPrice', models.FloatField()),
                ('OneBalcesPrice', models.FloatField(default=0)),
                ('CountBalces', models.FloatField(default=0)),
                ('Active', models.BooleanField(default=True)),
                ('PackageParts', models.ManyToManyField(related_name='PackageParts', to='novav1.pricing')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('Patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.patient')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novav1.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.patient'),
        ),
        migrations.AddField(
            model_name='order',
            name='Patient_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Patient_from', to='novav1.patient'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='novav1.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='PackageParts',
            field=models.ManyToManyField(blank=True, null=True, related_name='itemPackageParts', to='novav1.pricing'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novav1.category'),
        ),
        migrations.AddField(
            model_name='clinc',
            name='Device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.device'),
        ),
        migrations.AddField(
            model_name='clinc',
            name='Room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novav1.room'),
        ),
        migrations.CreateModel(
            name='ballses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.IntegerField()),
                ('ballses_count', models.IntegerField()),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novav1.patient')),
            ],
        ),
    ]
