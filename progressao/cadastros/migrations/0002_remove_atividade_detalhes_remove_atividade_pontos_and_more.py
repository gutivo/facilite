# Generated by Django 5.0 on 2023-12-22 13:22

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='detalhes',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='pontos',
        ),
        migrations.AddField(
            model_name='atividade',
            name='colaborador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Colaborador'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='prazo',
            field=models.DateField(default=datetime.date.today, verbose_name='Prazo Final'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='numero',
            field=models.CharField(max_length=45, verbose_name='Atribuição'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Órgão/Empresa'),
        ),
    ]
