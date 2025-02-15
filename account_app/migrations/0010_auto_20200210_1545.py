# Generated by Django 3.0.3 on 2020-02-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0009_auto_20200210_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subheadaccount',
            name='sub_head_account',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='subhead',
            unique_together={('head', 'sub_head')},
        ),
        migrations.AlterUniqueTogether(
            name='subheadaccount',
            unique_together={('sub_head', 'sub_head_account')},
        ),
        migrations.AlterIndexTogether(
            name='subhead',
            index_together={('head', 'sub_head')},
        ),
        migrations.AlterIndexTogether(
            name='subheadaccount',
            index_together={('sub_head', 'sub_head_account')},
        ),
    ]
