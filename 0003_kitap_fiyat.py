# Generated by Django 3.1 on 2020-08-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_kitap'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitap',
            name='fiyat',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
