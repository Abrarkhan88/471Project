# Generated by Django 5.1 on 2024-09-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0004_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.TextField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
