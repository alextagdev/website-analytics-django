# Generated by Django 4.1.2 on 2023-12-04 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_performanceanalysis_ip_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='performanceanalysis',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='performanceanalysis',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
