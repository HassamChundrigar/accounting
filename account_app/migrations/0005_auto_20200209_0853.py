# Generated by Django 3.0.3 on 2020-02-09 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0004_auto_20200209_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subentry',
            name='sub_head_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_app.SubHeadAccount'),
        ),
    ]
