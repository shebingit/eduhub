# Generated by Django 4.1 on 2023-05-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eduhub', '0014_enroll_ctype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer_box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('offer_dics', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='courseinternship_details',
        ),
    ]
