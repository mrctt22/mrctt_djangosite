# Generated by Django 4.2.6 on 2023-11-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qrgen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('contenuto', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='qrgen_images/')),
                ('note', models.TextField()),
            ],
        ),
    ]
