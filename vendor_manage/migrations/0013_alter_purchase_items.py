# Generated by Django 4.2.7 on 2023-12-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_manage', '0012_alter_purchase_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='items',
            field=models.JSONField(null=True),
        ),
    ]
