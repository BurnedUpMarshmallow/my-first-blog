# Generated by Django 4.2.4 on 2023-09-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
