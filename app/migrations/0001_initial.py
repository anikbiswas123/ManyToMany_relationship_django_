# Generated by Django 4.2.2 on 2023-06-20 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=100)),
                ('cus_email', models.EmailField(max_length=254, unique=True)),
                ('cus_mobile', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=100)),
                ('pro_qty', models.PositiveIntegerField()),
                ('cus', models.ManyToManyField(to='app.customer')),
            ],
        ),
    ]