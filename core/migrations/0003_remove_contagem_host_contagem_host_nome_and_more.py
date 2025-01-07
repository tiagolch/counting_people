# Generated by Django 5.1.4 on 2025-01-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_host_email_remove_host_telefone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contagem',
            name='host',
        ),
        migrations.AddField(
            model_name='contagem',
            name='host_nome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contagem',
            name='criancas',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='contagem',
            name='total_pessoas',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='contagem',
            name='visitantes',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Host',
        ),
    ]
