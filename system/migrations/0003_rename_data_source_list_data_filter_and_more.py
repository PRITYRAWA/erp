# Generated by Django 4.0 on 2023-01-31 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('system', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='data_source',
            new_name='data_filter',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='list',
            new_name='data_sort',
        ),
        migrations.RemoveField(
            model_name='list',
            name='sequence',
        ),
        migrations.AddField(
            model_name='list',
            name='default_view',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='list_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.choice'),
        ),
        migrations.AddField(
            model_name='list',
            name='primary_table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.table'),
        ),
        migrations.AddField(
            model_name='list',
            name='system_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='visibility',
            field=models.CharField(blank=True, choices=[('1', 'Required'), ('2', 'Optional'), ('3', 'Default')], max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ListSorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('column', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.column')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to='auth.user')),
                ('sort_direction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.choice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListFilters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to='auth.user')),
                ('data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.data')),
                ('operator_choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.choice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('system_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon_image', models.FileField(max_length=255, upload_to='icon_images/')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to='auth.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]