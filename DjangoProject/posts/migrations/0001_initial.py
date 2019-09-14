# Generated by Django 2.1.7 on 2019-03-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('c_date', models.DateField()),
                ('c_time', models.CharField(max_length=20)),
                ('thresh', models.CharField(max_length=10)),
                ('emb', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
