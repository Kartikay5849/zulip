# Generated by Django 5.0.9 on 2024-10-15 09:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0613_alter_realm_can_move_messages_between_channels_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="realm",
            name="move_messages_between_streams_policy",
        ),
    ]
