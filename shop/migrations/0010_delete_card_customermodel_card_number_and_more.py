# Generated by Django 4.2.3 on 2023-07-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_card_cvc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.AddField(
            model_name='customermodel',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='exp_month',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='exp_year',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
