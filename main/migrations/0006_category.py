# Generated by Django 5.1.1 on 2024-10-02 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]