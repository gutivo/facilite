# Generated by Django 5.0 on 2024-01-15 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0016_campo_agenteci_campo_agentecpl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campo',
            name='city',
            field=models.CharField(blank=True, max_length=150, verbose_name='Cidade'),
        ),
    ]