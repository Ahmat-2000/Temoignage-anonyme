# Generated by Django 4.2.7 on 2024-01-24 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("temoignageApp", "0006_remove_temoignesmodel_temoin_temoignesmodel_message"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="temoignesmodel",
            options={
                "verbose_name": "Témoignage",
                "verbose_name_plural": "Témoignages",
            },
        ),
        migrations.AlterModelTable(
            name="temoignesmodel",
            table="temoignages",
        ),
    ]
