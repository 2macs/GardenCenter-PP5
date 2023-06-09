# Generated by Django 4.2.1 on 2023-06-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MakeEnquiry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=75)),
                ("email", models.EmailField(max_length=254)),
                ("heading", models.CharField(max_length=250)),
                ("message_body", models.TextField()),
                ("acknowledged", models.BooleanField(default=False)),
                ("date_submitted", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-date_submitted", "acknowledged"],
                "indexes": [
                    models.Index(
                        fields=["-date_submitted"],
                        name="enquiry_mak_date_su_a04d83_idx",
                    )
                ],
            },
        ),
    ]
