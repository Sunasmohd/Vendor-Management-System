# Generated by Django 4.2.7 on 2023-12-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_manage', '0009_alter_historicalperformance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='items',
            field=models.JSONField(null=True),
        ),
    ]