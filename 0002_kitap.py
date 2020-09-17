# Generated by Django 3.1 on 2020-08-11 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kitap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('created', models.DateTimeField(verbose_name='created')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.yazar')),
            ],
        ),
    ]