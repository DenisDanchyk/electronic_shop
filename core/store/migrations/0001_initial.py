# Generated by Django 3.2.9 on 2021-11-05 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category')),
                ('slug', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of product')),
                ('description', models.TextField(verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('image', models.ImageField(upload_to='product_photo/')),
                ('guarantee', models.IntegerField(verbose_name='Guarantee (month)')),
                ('slug', models.SlugField(max_length=255)),
                ('in_order', models.BooleanField(default=False, verbose_name='The order is placed')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('communication_standard', models.CharField(choices=[('2G', '2G'), ('5G', '5G'), ('4G', '3G'), ('3G', '3G')], max_length=2, verbose_name='Communication standart')),
                ('matrix_type', models.CharField(choices=[('TFT-LCD', 'TFT-LSD'), ('CAPACITIVE TOUCHSCREEN LCD', 'CAPACITIVE TOUCHSCREEN LCD'), ('OLED', 'OLED'), ('IPS-LSD', 'IPS-LSD'), ('SUPER AMOLED', 'SUPER AMOLED'), ('AMOLED', 'AMOLED')], max_length=30, verbose_name='Type of matrix')),
                ('displat_diagonal', models.FloatField(verbose_name='Display diagonal')),
                ('display_resolution', models.CharField(max_length=15, verbose_name='Display resolution')),
                ('hz', models.IntegerField(verbose_name='Screen refresh rate (Hz)')),
                ('built_in_memory', models.IntegerField(verbose_name='Built-in memory (GB)')),
                ('operating_system', models.CharField(choices=[('IOS', 'IOS'), ('ANDROID', 'ANDROID')], max_length=30, verbose_name='Operating system')),
                ('main_camera_megapixels', models.IntegerField(verbose_name='The number of megapixels in the main camera')),
                ('front_camera_megapixels', models.IntegerField(verbose_name='The number of megapixels in the front camera')),
                ('additionally', models.TextField(blank=True, null=True, verbose_name='Additionally')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
            options={
                'verbose_name': 'Smartphone',
                'verbose_name_plural': 'Smartphones',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of product')),
                ('description', models.TextField(verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('image', models.ImageField(upload_to='product_photo/')),
                ('guarantee', models.IntegerField(verbose_name='Guarantee (month)')),
                ('slug', models.SlugField(max_length=255)),
                ('in_order', models.BooleanField(default=False, verbose_name='The order is placed')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('season', models.CharField(choices=[('SUMMER', 'SUMMER'), ('AUTUMN', 'AUTUMN'), ('SPRING', 'SPRING'), ('WINTER', 'WINTER')], max_length=6, verbose_name='Season')),
                ('country_of_origin', models.CharField(max_length=55, verbose_name='Країна виробник')),
                ('brand', models.CharField(max_length=55, verbose_name='Brand')),
                ('color', models.CharField(max_length=55, verbose_name='Color')),
                ('size', models.CharField(choices=[('44', '44'), ('40', '40'), ('36', '36'), ('43', '43'), ('38', '38'), ('41', '41'), ('37', '37'), ('42', '42'), ('39', '39')], max_length=3, verbose_name='Size')),
                ('material', models.CharField(max_length=100, verbose_name='Material')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
            options={
                'verbose_name': 'Shoes',
                'verbose_name_plural': 'Shoes',
            },
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of product')),
                ('description', models.TextField(verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('image', models.ImageField(upload_to='product_photo/')),
                ('guarantee', models.IntegerField(verbose_name='Guarantee (month)')),
                ('slug', models.SlugField(max_length=255)),
                ('in_order', models.BooleanField(default=False, verbose_name='The order is placed')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('peculiarities', models.CharField(max_length=255, verbose_name='Features')),
                ('material', models.CharField(max_length=100, verbose_name='Material')),
                ('color', models.CharField(max_length=55, verbose_name='Color')),
                ('size', models.CharField(max_length=55, verbose_name='Size')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('weight', models.IntegerField(verbose_name='Weight')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
            options={
                'verbose_name': 'Furniture',
                'verbose_name_plural': 'Furniture',
            },
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of product')),
                ('description', models.TextField(verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('image', models.ImageField(upload_to='product_photo/')),
                ('guarantee', models.IntegerField(verbose_name='Guarantee (month)')),
                ('slug', models.SlugField(max_length=255)),
                ('in_order', models.BooleanField(default=False, verbose_name='The order is placed')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('computer_or_laptop', models.CharField(choices=[('Laptop', 'Laptop'), ('Computer', 'Computer')], max_length=10)),
                ('brief_technical_characteristics', models.CharField(max_length=255, verbose_name='Brief technical characteristics')),
                ('ram_size', models.CharField(max_length=255, verbose_name='Ram size')),
                ('motherboard', models.CharField(max_length=255, verbose_name='Matherboard')),
                ('cpu', models.CharField(max_length=255, verbose_name='Processor')),
                ('bp', models.CharField(max_length=255, verbose_name='Power Supply')),
                ('vedio_card', models.CharField(max_length=255, verbose_name='Video card')),
                ('hdd', models.CharField(max_length=255, verbose_name='HDD')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
            options={
                'verbose_name': 'Computer',
                'verbose_name_plural': 'Computers',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of product')),
                ('description', models.TextField(verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('image', models.ImageField(upload_to='product_photo/')),
                ('guarantee', models.IntegerField(verbose_name='Guarantee (month)')),
                ('slug', models.SlugField(max_length=255)),
                ('in_order', models.BooleanField(default=False, verbose_name='The order is placed')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('brand', models.CharField(max_length=55, verbose_name='Brand')),
                ('gender', models.CharField(choices=[('MAN', 'MAN'), ('WOMAN', 'WOMAN')], max_length=5, verbose_name='Gender')),
                ('color', models.CharField(max_length=55, verbose_name='Color')),
                ('size', models.CharField(choices=[('XXL', 'XXL'), ('XL', 'XL'), ('M', 'M'), ('S', 'S'), ('L', 'L')], max_length=3, verbose_name='Size')),
                ('material', models.CharField(max_length=100, verbose_name='Material')),
                ('country_of_origin', models.CharField(max_length=55, verbose_name='Country of origin')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
            options={
                'verbose_name': 'Clothes',
                'verbose_name_plural': 'Clothes',
            },
        ),
    ]