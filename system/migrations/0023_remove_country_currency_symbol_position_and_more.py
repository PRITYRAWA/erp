# Generated by Django 4.0 on 2023-02-08 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0022_rename_telephone_country_telephone_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='currency_symbol_position',
        ),
        migrations.AddField(
            model_name='country',
            name='symbol_position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_symbol_position', to='system.choice'),
        ),
        migrations.AlterField(
            model_name='country',
            name='date_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_date_format', to='system.choice'),
        ),
        migrations.AlterField(
            model_name='country',
            name='money_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_money_format', to='system.choice'),
        ),
        migrations.AlterField(
            model_name='country',
            name='time_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_time_format', to='system.choice'),
        ),
    ]