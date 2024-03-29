# Generated by Django 4.2.7 on 2024-02-26 03:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendartimely', '0002_event_repeat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='repeat',
        ),
        migrations.AddField(
            model_name='event',
            name='repeat_frequency',
            field=models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='repeat_interval',
            field=models.IntegerField(default=1),
        ),
    ]
