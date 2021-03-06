# Generated by Django 4.0 on 2021-12-15 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_question_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('door_no', models.IntegerField(blank=True, null=True)),
                ('city', models.TextField()),
                ('customer_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.customer')),
            ],
        ),
    ]
