# Generated by Django 5.1.3 on 2024-11-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_items_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.ImageField(upload_to='work/'),
        ),
    ]
