# Generated by Django 2.0 on 2020-05-02 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20200502_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='size',
        ),
    ]