# Generated by Django 2.2.6 on 2019-10-18 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zezere', '0003_auto_20191017_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='runrequest',
            name='initrd_url',
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                validators=[django.core.validators.URLValidator],  # type: ignore
                verbose_name='InitRD URL'
            ),
        ),
        migrations.AddField(
            model_name='runrequest',
            name='kernel_cmd',
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name='Kernel Command Line'
            ),
        ),
    ]
