# Generated by Django 4.1.1 on 2022-09-12 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approvals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('dependants', models.IntegerField(default=0)),
                ('applicantincome', models.IntegerField(default=0)),
                ('coapplicantincome', models.IntegerField(default=0)),
                ('loanamt', models.IntegerField(default=0)),
                ('loanterm', models.IntegerField(default=0)),
                ('credithistory', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('graduatededucation', models.CharField(choices=[('Graduate', 'Graduate'), ('Not_Graduate', 'Not_Graduate')], max_length=20)),
                ('selfemployed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')], max_length=20)),
            ],
        ),
    ]