# Generated by Django 3.2.9 on 2022-01-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=50)),
                ('sana', models.DateField()),
                ('batafsil', models.TextField(max_length=100)),
                ('status', models.CharField(choices=[('active', 'active'), ('soon', 'soon'), ('done', 'done')], max_length=10)),
            ],
        ),
    ]
