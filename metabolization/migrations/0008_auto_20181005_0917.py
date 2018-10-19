# Generated by Django 2.1.2 on 2018-10-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metabolization', '0007_auto_20181004_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='method_priority',
            field=models.CharField(choices=[('reactor', 'Reactor'), ('rdkit', 'RDKit')], default='rdkit', max_length=32),
        ),
    ]