# Generated by Django 3.0.7 on 2020-06-07 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200607_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='JamesDick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Length', models.FloatField(max_length=255)),
                ('Girth', models.FloatField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
