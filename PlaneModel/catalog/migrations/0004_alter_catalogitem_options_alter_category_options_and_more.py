# Generated by Django 4.0.5 on 2022-06-17 15:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_catalogitem_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogitem',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='catalogitem',
            name='item_image',
        ),
        migrations.RemoveField(
            model_name='catalogitem',
            name='item_info',
        ),
        migrations.RemoveField(
            model_name='catalogitem',
            name='item_weight',
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='edit_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date of edit product'),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='publication_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date of publication'),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='weight',
            field=models.FloatField(default=0.0, verbose_name='weight'),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='category',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='catalog.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='price',
            field=models.FloatField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='catalog.category', verbose_name='Parent '),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='image')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.catalogitem')),
            ],
        ),
    ]
