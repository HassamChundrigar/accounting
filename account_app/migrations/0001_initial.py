# Generated by Django 3.0.3 on 2020-02-04 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(choices=[('Asset', 'Asset'), ('Expense', 'Expense'), ('Liability', 'Liability'), ('Revenue', 'Revenue'), ('Equity', 'Equity')], max_length=15)),
                ('sub_head', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('subhead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.SubHead')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dated', models.DateField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('credit', models.ManyToManyField(related_name='credit', to='account_app.SubEntry')),
                ('debit', models.ManyToManyField(related_name='debit', to='account_app.SubEntry')),
            ],
        ),
    ]
