# Generated by Django 3.2.14 on 2022-07-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eos', '0010_auto_20220718_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_list',
            name='od_date',
            field=models.CharField(max_length=200),
        ),
    ]