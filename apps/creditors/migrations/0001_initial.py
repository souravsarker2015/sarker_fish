# Generated by Django 4.2.13 on 2024-06-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creditor_name', models.CharField(max_length=255)),
                ('creditor_type', models.CharField(choices=[('bank', 'Bank'), ('individual', 'Individual'), ('corporation', 'Corporation'), ('shop', 'Shop')], max_length=30)),
                ('credit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
