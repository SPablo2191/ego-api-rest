# Generated by Django 4.2.11 on 2024-03-13 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("car_dealership_api", "0003_remove_feature_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feature",
            name="data_sheet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="data_sheet_feature",
                to="car_dealership_api.datasheet",
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="data_sheet",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="data_sheet_section",
                to="car_dealership_api.datasheet",
            ),
        ),
    ]
