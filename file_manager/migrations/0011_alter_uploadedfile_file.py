# Generated by Django 5.0.1 on 2024-10-01 10:08

import django.core.files.storage
import django.core.files.storage.filesystem
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0010_rename_long_description_uploadedfile_long_reference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=django.core.files.storage.filesystem.FileSystemStorage.path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'mp4', 'avi', 'mov', 'pdf', 'png', 'jpg', 'jpeg'])]),
        ),
    ]
