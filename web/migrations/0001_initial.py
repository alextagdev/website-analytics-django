# Generated by Django 4.1.2 on 2023-12-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('load_time', models.FloatField()),
                ('request_count', models.IntegerField()),
                ('file_size', models.FloatField()),
                ('server_response_time', models.FloatField()),
            ],
        ),
    ]