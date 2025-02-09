# Generated by Django 5.1.4 on 2025-01-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='email',
        ),
        migrations.RemoveField(
            model_name='host',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='host',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='contagem',
            name='criancas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contagem',
            name='total_pessoas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contagem',
            name='visitantes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
