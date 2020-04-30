# Generated by Django 2.0 on 2020-04-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200430_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(choices=[('1', 'S'), ('2', 'M'), ('3', 'L'), ('4', 'XL'), ('5', 'XXL'), ('6', 'XXXL')], default='3', max_length=20),
        ),
    ]