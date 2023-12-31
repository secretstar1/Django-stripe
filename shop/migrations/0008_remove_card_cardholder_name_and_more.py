# Generated by Django 4.2.3 on 2023-07-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_customermodel_id1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='cardholder_name',
        ),
        migrations.RemoveField(
            model_name='card',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='card',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='card',
            name='exp_month',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='exp_year',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='cvc',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
