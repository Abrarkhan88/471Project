# Generated by Django 5.0.6 on 2024-09-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0006_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review_box',
            field=models.TextField(max_length=500),
        ),
    ]
