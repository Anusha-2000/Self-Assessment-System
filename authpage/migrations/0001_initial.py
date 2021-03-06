# Generated by Django 3.1.5 on 2021-06-14 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=100)),
                ('ln', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('usr_nm', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=10)),
                ('sem_no', models.IntegerField(default=1)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL'), ('EEE', 'EEE')], default='CSE', max_length=100)),
            ],
        ),
    ]
