# Generated by Django 4.1 on 2023-05-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eduhub', '0010_enquir_rename_enquiry_enroll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquir',
            name='enq_status',
            field=models.CharField(blank=True, default='0', max_length=50, null=True),
        ),
    ]
