# Generated by Django 4.0 on 2023-02-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0015_remove_choice_editable_alter_choice_deafult_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
    ]
