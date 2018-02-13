# Generated by Django 2.0.1 on 2018-02-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additem',
            old_name='name',
            new_name='business_name',
        ),
        migrations.RenameField(
            model_name='additem',
            old_name='date',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='additem',
            name='description',
            field=models.TextField(default='write a description text'),
        ),
    ]