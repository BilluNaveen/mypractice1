# Generated by Django 4.0 on 2021-12-15 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_question_text_question_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='customer',
        ),
    ]
