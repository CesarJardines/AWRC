# Generated by Django 3.2.5 on 2021-09-02 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AMCE', '0014_alter_anadir_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votar',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
