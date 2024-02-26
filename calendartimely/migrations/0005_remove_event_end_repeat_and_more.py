# Generated by Django 4.2.7 on 2024-02-26 03:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendartimely', '0004_event_end_repeat_alter_event_repeat_frequency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_repeat',
        ),
        migrations.RemoveField(
            model_name='event',
            name='repeat_frequency',
        ),
        migrations.RemoveField(
            model_name='event',
            name='repeat_interval',
        ),
        migrations.AddField(
            model_name='event',
            name='repeat',
            field=models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
