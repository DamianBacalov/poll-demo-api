# Generated by Django 3.2.5 on 2021-07-26 12:32

from django.db import migrations
from django.conf import settings

def populate_poll(apps, schema_editor):
    Option = apps.get_model('api', 'VotingOption')
    poll_type = settings.POLL_TYPE
    poll_options = settings.POLL_OPTIONS[poll_type]

    for op in poll_options:
        Option.objects.create(name=op,votes=0)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_poll),
    ]
