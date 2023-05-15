# Generated by Django 4.1 on 2023-05-15 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eduhub', '0003_delete_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('place', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('stream', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('pasout_year', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('expe', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('expe_no', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('message', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('designation', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('enq_status', models.CharField(default=0, max_length=50, null=True)),
                ('enq_date', models.DateField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Eduhub.course_details')),
            ],
        ),
    ]
