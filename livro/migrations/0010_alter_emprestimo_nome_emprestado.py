# Generated by Django 4.2.6 on 2023-10-17 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('livro', '0009_emprestimo_nome_emprestado_anonimo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.usuario'),
        ),
    ]