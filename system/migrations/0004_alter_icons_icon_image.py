# Generated by Django 4.0 on 2023-01-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_rename_data_source_list_data_filter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icons',
            name='icon_image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='icon_images/'),
        ),
    ]
