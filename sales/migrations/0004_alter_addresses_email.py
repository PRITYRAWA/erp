# Generated by Django 4.0 on 2023-02-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]