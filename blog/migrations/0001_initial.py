# Generated by Django 5.1 on 2024-09-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='enter title news')),
                ('image', models.ImageField(upload_to='post/', verbose_name='download picture')),
                ('description', models.TextField(verbose_name='white your news')),
                ('url_news', models.URLField(verbose_name='white your url news')),
                ('email_news', models.EmailField(max_length=254, verbose_name='white  email news company')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
