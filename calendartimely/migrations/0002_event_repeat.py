# Generated by Django 4.2.7 on 2024-02-26 02:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendartimely', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='repeat',
            field=models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
