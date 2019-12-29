# Generated by Django 3.0.1 on 2019-12-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=50, null=True)),
                ('last_Name', models.CharField(max_length=50, null=True)),
                ('email_Address', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_title', models.CharField(max_length=50, null=True)),
                ('img_description', models.TextField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]