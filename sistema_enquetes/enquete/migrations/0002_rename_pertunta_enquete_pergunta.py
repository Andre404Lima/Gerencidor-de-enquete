# Generated by Django 5.2.3 on 2025-06-18 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquete',
            old_name='pertunta',
            new_name='pergunta',
        ),
    ]
