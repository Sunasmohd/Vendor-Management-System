# Generated by Django 4.2.7 on 2023-12-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_manage', '0010_alter_purchase_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(default=0, null=True),
        ),
    ]
