# Generated by Django 4.1.2 on 2022-10-25 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]