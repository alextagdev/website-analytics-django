# Generated by Django 4.1.2 on 2023-12-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_performanceanalysis_load_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performanceanalysis',
            name='file_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='performanceanalysis',
            name='request_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='performanceanalysis',
            name='server_response_time',
            field=models.FloatField(default=0.0),
        ),
    ]