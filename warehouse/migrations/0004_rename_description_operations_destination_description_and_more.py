# Generated by Django 4.0 on 2023-01-06 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_delete_product_lines'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operations',
            old_name='description',
            new_name='destination_description',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='operations',
            name='origin',
        ),
        migrations.AddField(
            model_name='operations',
            name='origin_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transfers',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destination', to='warehouse.locations'),
        ),
        migrations.AddField(
            model_name='transfers',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origin', to='warehouse.locations'),
        ),
        migrations.AlterField(
            model_name='routes',
            name='route_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
