# Generated by Django 4.2.9 on 2024-02-11 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='dish',
        ),
    ]