# Generated by Django 3.2.5 on 2021-10-31 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название продукта')),
                ('count', models.IntegerField(verbose_name='Проданное количество')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('income', models.BigIntegerField(verbose_name='Прибыль')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TotalIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bill', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ArchiveIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive_count', models.IntegerField()),
                ('archive_bill', models.BigIntegerField()),
                ('archive_income', models.BigIntegerField(verbose_name='Прибыль')),
                ('archive_created_at', models.DateTimeField(auto_now_add=True)),
                ('archive_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
