# Generated by Django 4.1 on 2023-05-16 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eduhub', '0007_courseinternship_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='courojt_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_subhead', models.CharField(blank=True, max_length=255, null=True)),
                ('course_subetails', models.TextField(blank=True, default='', null=True)),
                ('course_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Eduhub.course_details')),
            ],
        ),
        migrations.CreateModel(
            name='courseojt_points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseojt_points', models.TextField(blank=True, default='', null=True)),
                ('courseojt_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Eduhub.courojt_details')),
            ],
        ),
    ]
