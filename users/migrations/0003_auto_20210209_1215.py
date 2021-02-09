# Generated by Django 3.1.6 on 2021-02-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210209_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='myModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lapName', models.CharField(max_length=20)),
                ('laplast', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]