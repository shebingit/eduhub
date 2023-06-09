# Generated by Django 4.1 on 2023-05-17 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eduhub', '0012_enquir_enq_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_details',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='course_details',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='course_details',
            name='type',
        ),
        migrations.CreateModel(
            name='Course_catgeorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, max_length=50, null=True)),
                ('Offer_Head', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('Offer_Fee', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('Fee', models.IntegerField(blank=True, null=True)),
                ('Duration', models.CharField(blank=True, max_length=100, null=True)),
                ('Start_date', models.DateField(blank=True, null=True)),
                ('Cate_course_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Eduhub.course_details')),
            ],
        ),
    ]
