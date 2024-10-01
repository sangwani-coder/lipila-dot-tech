# Generated by Django 5.0.1 on 2024-09-30 12:15

import django.core.files.storage
import django.core.files.storage.filesystem
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0009_alter_uploadedfile_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedfile',
            old_name='long_description',
            new_name='long_reference',
        ),
        migrations.RenameField(
            model_name='uploadedfile',
            old_name='short_description',
            new_name='short_reference',
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=django.core.files.storage.filesystem.FileSystemStorage.path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'mp4', 'avi', 'mov', 'pdf', 'png', 'jpg', 'jpeg'])]),
        ),
    ]
