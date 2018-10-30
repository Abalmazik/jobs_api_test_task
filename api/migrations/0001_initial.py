# Generated by Django 2.1.2 on 2018-10-30 10:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('title_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('importance', models.FloatField()),
                ('level', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='api.Skill'),
        ),
    ]