# Generated by Django 3.0.8 on 2020-08-08 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_newsstory_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story', to=settings.AUTH_USER_MODEL),
        ),
    ]
