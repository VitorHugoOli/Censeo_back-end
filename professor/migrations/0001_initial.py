# Generated by Django 3.0.7 on 2020-06-15 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('idprofessor', models.IntegerField(db_column='idProfessor', primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=45, null=True)),
                ('username', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('login', models.CharField(blank=True, max_length=45, null=True)),
                ('senha', models.CharField(max_length=45)),
                ('lattes', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Professor',
                'managed': False,
            },
        ),
    ]