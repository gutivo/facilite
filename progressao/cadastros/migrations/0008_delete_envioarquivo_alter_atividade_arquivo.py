# Generated by Django 5.0 on 2023-12-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_atividade_arquivo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EnvioArquivo',
        ),
        migrations.AlterField(
            model_name='atividade',
            name='arquivo',
            field=models.FileField(upload_to='pdf/', verbose_name='Anexos'),
        ),
    ]
