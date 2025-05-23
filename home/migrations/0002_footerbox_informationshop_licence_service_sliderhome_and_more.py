# Generated by Django 5.1.6 on 2025-02-20 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'باکس فوتر',
                'verbose_name_plural': 'باکس های فوتر',
            },
        ),
        migrations.CreateModel(
            name='InformationShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='تلگرام')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='اینستاگرام')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='واتساپ')),
                ('email', models.URLField(blank=True, null=True, verbose_name='ایمیل')),
                ('phone_number', models.CharField(max_length=11, verbose_name='شماره تلفن')),
                ('address', models.CharField(max_length=500, verbose_name='آدرس')),
            ],
            options={
                'verbose_name': 'جزییات اطلاعات',
                'verbose_name_plural': 'اطلاعات فروشگاه',
            },
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان مجوز')),
                ('image', models.ImageField(upload_to='images/licence', verbose_name='عکس مجوز')),
                ('url', models.URLField(blank=True, null=True, verbose_name='لینک مجوز')),
            ],
            options={
                'verbose_name': 'مجوز',
                'verbose_name_plural': 'مجوز ها',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/icon_service', verbose_name='آیکن')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('desc', models.CharField(max_length=250, verbose_name='توضیح خیلی کوتاه')),
            ],
            options={
                'verbose_name': 'خدمات',
                'verbose_name_plural': 'خدمات',
            },
        ),
        migrations.CreateModel(
            name='SliderHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='عنوان اسلایدر')),
                ('image', models.ImageField(upload_to='images/slider', verbose_name='تصویر')),
                ('url', models.URLField(blank=True, null=True, verbose_name='لینک')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان لینک')),
                ('url', models.URLField(verbose_name='لینک یو آر ال')),
                ('footer_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer', to='home.footerbox', verbose_name='باکس فوتر')),
            ],
            options={
                'verbose_name': 'لینک فوتر',
                'verbose_name_plural': 'لینک های فوتر',
            },
        ),
    ]
