# Generated by Django 2.1.5 on 2019-02-15 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='City.city +', to='users.Post'),
        ),
    ]