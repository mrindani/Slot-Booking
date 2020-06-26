# Generated by Django 3.0.7 on 2020-06-26 04:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventId', models.CharField(default='LECXXX', max_length=8, primary_key='true', serialize=False)),
                ('eventName', models.CharField(blank='false', max_length=50)),
                ('eventDesc', models.TextField(default='Event or Lecture', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userName', models.CharField(blank='false', max_length=100, primary_key='true', serialize=False)),
                ('userId', models.IntegerField()),
                ('userType', models.CharField(choices=[('Admin', 'admin'), ('Faculty', 'faculty'), ('Club', 'club')], default='Faculty', max_length=10)),
                ('userMailId', models.CharField(default='@ahduni.edu.in', max_length=100)),
                ('userPassword', models.CharField(blank='false', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rSlot', models.CharField(default='1', max_length=15)),
                ('rDate', models.CharField(default=' ', max_length=20)),
                ('rRoom', models.CharField(default='005', max_length=10)),
                ('reqStatus', models.CharField(choices=[('Accepted', 'accept'), ('Declined', 'decline')], default='Declined', max_length=10)),
                ('fbDesc', models.TextField()),
                ('rEvent', models.ForeignKey(default='LEC', on_delete=django.db.models.deletion.SET_DEFAULT, to='slot.Event')),
                ('rUser', models.ForeignKey(default='faculty', on_delete=django.db.models.deletion.SET_DEFAULT, to='slot.User')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='eUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='slot.User'),
        ),
        migrations.CreateModel(
            name='RoomSlot',
            fields=[
                ('rsId', models.AutoField(primary_key=True, serialize=False)),
                ('slotId', models.CharField(choices=[('9.30-11', '9.30 - 11'), ('11-12.30', '11 - 12.30'), ('1-2.30', '1 - 2.30'), ('2.30-4', '2.30 - 4'), ('4-5.30', '4 - 5.30'), ('5.30-7', '5.30 - 7')], default='1', max_length=10)),
                ('roomNum', models.CharField(choices=[('001', '001'), ('005', '005'), ('105', '105'), ('116', '116')], default='005', max_length=10)),
                ('roomType', models.CharField(choices=[('Classroom', 'classroom'), ('Lab', 'lab'), ('Auditorium', 'auditorium')], default='Classroom', max_length=10)),
                ('roomCapacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(25), django.core.validators.MaxValueValidator(300)])),
                ('slotDate', models.DateField(auto_now=True)),
                ('rsUserName', models.ForeignKey(default='faculty', on_delete=django.db.models.deletion.SET_DEFAULT, to='slot.User')),
            ],
            options={
                'unique_together': {('slotId', 'roomNum', 'slotDate')},
            },
        ),
    ]