# Generated by Django 4.2.7 on 2023-11-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('fa', 'Persian'), ('en', 'English')], default='en', max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
