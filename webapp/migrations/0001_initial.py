# Generated by Django 5.0.4 on 2024-04-29 23:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('courses', models.ManyToManyField(related_name='students', to='webapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.professor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.student')),
            ],
        ),
    ]
