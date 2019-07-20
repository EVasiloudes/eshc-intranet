# Generated by Django 2.1.10 on 2019-07-20 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_auto_20190720_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apply.ApplicationSession', verbose_name='Application session'),
        ),
    ]
