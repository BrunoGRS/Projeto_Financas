# Generated by Django 4.2.3 on 2023-07-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=40)),
                ('banco', models.CharField(choices=[('NU', 'Nubank'), ('BD', 'Bradesco'), ('CE', 'Caixa Econômica'), ('SB', 'Sicoob'), ('SA', 'Santander')], max_length=2)),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
                ('valor', models.FloatField()),
                ('icone', models.ImageField(upload_to='icones')),
            ],
        ),
    ]
