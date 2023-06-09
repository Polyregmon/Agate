# Generated by Django 4.2.1 on 2023-05-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmenu',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
