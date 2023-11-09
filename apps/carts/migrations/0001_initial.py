# Generated by Django 4.2.7 on 2023-11-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("user_email", models.EmailField(max_length=254)),
                ("product_id", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name": "Cart Item",
                "verbose_name_plural": "Cart Items",
                "unique_together": {("user_email", "product_id")},
            },
        ),
    ]
