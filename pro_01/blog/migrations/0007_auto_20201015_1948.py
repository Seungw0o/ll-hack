# Generated by Django 3.1.2 on 2020-10-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_qr_code_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
