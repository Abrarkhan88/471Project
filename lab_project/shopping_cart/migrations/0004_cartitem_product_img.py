# Generated by Django 5.0.6 on 2024-09-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0003_cartitem_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product_img',
            field=models.ImageField(default='NULL', upload_to=''),
            preserve_default=False,
        ),
    ]
