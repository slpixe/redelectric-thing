# Generated by Django 3.0.7 on 2020-07-05 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anime', '0012_franchiseitemuser_area_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='franchiseitem',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]