# Generated by Django 2.0 on 2020-05-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20200502_1721'),
        ('cart', '0006_delete_colorsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, null=True, to='store.Variation'),
        ),
    ]
