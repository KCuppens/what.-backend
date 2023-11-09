# Generated by Django 4.2.7 on 2023-11-09 08:39

from django.db import migrations, models

from ..tests.factories import ProductFactory


def generate_demo_products(apps, schema_editor):
    ProductFactory.create_batch(5)


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ("name",),
            },
        ),
        migrations.RunPython(generate_demo_products, migrations.RunPython.noop),
    ]