# Generated by Django 4.2.7 on 2023-12-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('PN', 'Pending'), ('CN', 'Canceled'), ('CM', 'Completed')], max_length=2),
        ),
    ]
