# Generated by Django 2.2.2 on 2019-07-05 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20190704_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='building',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
