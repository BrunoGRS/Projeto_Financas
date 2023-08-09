# Generated by Django 4.2.3 on 2023-07-07 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0002_conta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], max_length=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.categoria')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.conta')),
            ],
        ),
    ]
