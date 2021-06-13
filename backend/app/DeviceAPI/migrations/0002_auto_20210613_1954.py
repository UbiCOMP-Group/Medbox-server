# Generated by Django 3.0 on 2021-06-13 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DeviceAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_devices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='device',
            name='supervisors',
            field=models.ManyToManyField(blank=True, related_name='supervised_devices', to=settings.AUTH_USER_MODEL),
        ),
    ]
