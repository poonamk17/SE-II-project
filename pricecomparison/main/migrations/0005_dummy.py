# Generated by Django 3.2.10 on 2022-04-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='dummy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.CharField(max_length=70)),
                ('imag_url', models.CharField(max_length=512)),
                ('linkA', models.CharField(max_length=1070)),
                ('linkF', models.CharField(max_length=1070)),
                ('linkC', models.CharField(max_length=1070)),
                ('amazonP', models.IntegerField()),
                ('flipkartP', models.IntegerField()),
                ('cromaP', models.IntegerField()),
            ],
        ),
    ]
