# Generated by Django 4.2.6 on 2023-10-17 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('livro', '0006_livros_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='usuario',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.usuario'),
            preserve_default=False,
        ),
    ]
