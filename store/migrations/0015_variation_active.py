# Generated by Django 2.0 on 2020-05-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_variation_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
