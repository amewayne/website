# Generated by Django 3.1.6 on 2021-02-20 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('ts_created', models.DateTimeField(auto_now_add=True)),
                ('ts_changed', models.DateTimeField(blank=True, null=True)),
                ('is_publish', models.BooleanField(default=False, verbose_name='是否发布')),
                ('ts_publish', models.DateTimeField(blank=True, null=True)),
                ('home_push', models.BooleanField(default=False, verbose_name='是否首页推送')),
                ('language', models.CharField(blank=True, max_length=32, null=True)),
                ('hit_count', models.IntegerField(default=0, verbose_name='点击量')),
                ('source', models.TextField(blank=True, max_length=5000, null=True)),
                ('thumb', models.CharField(blank=True, max_length=128, null=True, verbose_name='缩略图')),
            ],
            options={
                'db_table': 'archive',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_cn', models.CharField(blank=True, max_length=50, null=True)),
                ('title_en', models.CharField(blank=True, max_length=50, null=True)),
                ('ts_created', models.DateTimeField(auto_now=True)),
                ('is_pub', models.BooleanField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=32, null=True)),
                ('fid', models.CharField(blank=True, max_length=32, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='ArchiveI18n',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=50, verbose_name='语言')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, max_length=5000, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('ts_created', models.DateTimeField(auto_now_add=True)),
                ('ts_updated', models.DateTimeField(auto_now=True)),
                ('archive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.archive')),
            ],
            options={
                'db_table': 'archive_i18n',
            },
        ),
        migrations.CreateModel(
            name='ArchiveCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.archive')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.category')),
            ],
            options={
                'db_table': 'archive_category',
                'unique_together': {('aid', 'cid')},
            },
        ),
        migrations.AddField(
            model_name='archive',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', through='archive.ArchiveCategory', to='archive.Category'),
        ),
        migrations.AddField(
            model_name='archive',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
