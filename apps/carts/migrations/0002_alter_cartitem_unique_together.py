# Generated by Django 4.2.7 on 2023-11-09 10:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="cartitem",
            unique_together=set(),
        ),
    ]