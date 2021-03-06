# Generated by Django 3.1.5 on 2021-02-26 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100)),
                ('origin_name', models.CharField(max_length=50)),
                ('file_type', models.CharField(default='other', max_length=15)),
                ('ts_created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachment_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'attachment',
            },
        ),
    ]
