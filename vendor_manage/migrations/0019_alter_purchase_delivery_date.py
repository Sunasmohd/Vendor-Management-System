# Generated by Django 4.2.7 on 2023-12-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_manage', '0018_alter_historicalperformance_average_response_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='delivery_date',
            field=models.DateTimeField(),
        ),
    ]
