# Generated by Django 3.0.6 on 2020-05-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first', '0004_delete_travel'),
    ]

    operations = [
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
