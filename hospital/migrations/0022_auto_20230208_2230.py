# Generated by Django 3.0.5 on 2023-02-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_auto_20230208_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Senior scan doctor', 'Senior scan doctor'), ('Junior scan docotr', 'Junior scan docotr'), ('Senior neurologist', 'Senior neurologist'), ('Junior neurologist', 'Junior neurologist'), ('Senior neurosurgeon', 'Senior neurosurgeon'), ('Junior neurosurgeon', 'Senior neurosurgeon')], default='Junior neurosurgeon', max_length=50),
        ),
    ]
