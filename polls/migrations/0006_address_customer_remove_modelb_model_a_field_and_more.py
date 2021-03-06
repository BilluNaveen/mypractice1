# Generated by Django 4.0 on 2021-12-15 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_modela_modelb_delete_address_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(blank=True, max_length=70, null=True)),
                ('pin', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('age', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='modelb',
            name='model_a_field',
        ),
        migrations.DeleteModel(
            name='ModelA',
        ),
        migrations.DeleteModel(
            name='ModelB',
        ),
        migrations.AddField(
            model_name='address',
            name='model_a_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_b_field', to='polls.customer'),
        ),
    ]
