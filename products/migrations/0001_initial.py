# Generated by Django 4.2.2 on 2024-05-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price_purchase', models.DecimalField(decimal_places=0, max_digits=10)),
                ('price_sale', models.DecimalField(decimal_places=0, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('quantity_sold', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
