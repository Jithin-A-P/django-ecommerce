# Generated by Django 2.2 on 2021-02-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a text description'),
            preserve_default=False,
        ),
    ]
