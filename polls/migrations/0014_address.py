# Generated by Django 4.0 on 2021-12-16 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_customer_email_alter_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.TextField(null=True)),
                ('customer_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='polls.customer')),
            ],
        ),
    ]
