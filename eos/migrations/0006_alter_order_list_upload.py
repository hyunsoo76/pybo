# Generated by Django 3.2.14 on 2022-07-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eos', '0005_auto_20220707_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_list',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
