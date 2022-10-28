# Generated by Django 4.1 on 2022-10-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('remote_address', models.CharField(max_length=16, null=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
