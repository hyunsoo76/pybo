# Generated by Django 3.2.14 on 2022-07-15 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eos', '0008_alter_order_list_buyer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_list',
            name='d_day',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
