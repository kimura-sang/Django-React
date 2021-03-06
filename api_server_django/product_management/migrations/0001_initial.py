# Generated by Django 3.1.7 on 2021-05-12 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category_management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=255, verbose_name='asin')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('url', models.TextField(verbose_name='url')),
                ('own_description', models.TextField(verbose_name='description')),
                ('is_prime', models.BooleanField(verbose_name='is_prime')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='update_time')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductProposer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category_management.category')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_management.product')),
            ],
            options={
                'db_table': 'productproposer',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='price')),
                ('seller', models.CharField(max_length=255, verbose_name='seller')),
                ('shipper', models.CharField(max_length=255, verbose_name='shipper')),
                ('stocks', models.IntegerField(default=0, verbose_name='stocks')),
                ('stocks_status', models.IntegerField(default=0, verbose_name='stocks_status')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_management.product')),
            ],
            options={
                'db_table': 'productinfo',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(verbose_name='url')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_management.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_management.product')),
            ],
            options={
                'db_table': 'descriptions',
            },
        ),
    ]
