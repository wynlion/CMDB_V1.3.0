# Generated by Django 3.1.3 on 2021-04-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_auto_20210401_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=10)),
                ('text', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='media/image')),
                ('file_upload', models.FileField(upload_to='media/file')),
            ],
        ),
    ]