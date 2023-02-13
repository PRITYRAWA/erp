# Generated by Django 4.0 on 2023-02-08 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0021_remove_configuration_category_configuration_editable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='telephone',
            new_name='telephone_code',
        ),
        migrations.AddField(
            model_name='country',
            name='currency_symbol_position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_symbol_position', to='system.selectors'),
        ),
        migrations.AddField(
            model_name='country',
            name='date_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_date_format', to='system.selectors'),
        ),
        migrations.AddField(
            model_name='country',
            name='money_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_money_format', to='system.selectors'),
        ),
        migrations.AddField(
            model_name='country',
            name='native_name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='country',
            name='time_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_time_format', to='system.selectors'),
        ),
    ]