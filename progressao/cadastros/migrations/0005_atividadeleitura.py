# Generated by Django 5.0 on 2023-12-22 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_atividade_data_alter_atividade_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeLeitura',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('cadastros.atividade',),
        ),
    ]
