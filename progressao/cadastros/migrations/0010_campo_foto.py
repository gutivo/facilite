# Generated by Django 5.0 on 2023-12-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='campo',
            name='foto',
            field=models.ImageField(default=1, upload_to='imagens/'),
            preserve_default=False,
        ),
    ]
