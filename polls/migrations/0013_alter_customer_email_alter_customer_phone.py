# Generated by Django 4.0 on 2021-12-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_alter_customer_email_alter_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
