# Generated by Django 2.2.2 on 2019-07-13 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0030_auto_20190713_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User', to_field='user_id'),
        ),
    ]
