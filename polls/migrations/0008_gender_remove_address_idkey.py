# Generated by Django 4.0 on 2021-12-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_address_idkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='address',
            name='idkey',
        ),
    ]
