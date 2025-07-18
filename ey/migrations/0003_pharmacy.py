# Generated by Django 5.2.4 on 2025-07-09 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ey', '0002_patientdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('pharmacyid', models.AutoField(primary_key=True, serialize=False)),
                ('DoctorName', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=150)),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(max_length=20)),
                ('Description', models.TextField()),
                ('Qty', models.IntegerField()),
                ('Total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ey.patientdetails')),
            ],
        ),
    ]
