# Generated by Django 5.0.6 on 2024-06-28 14:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                (
                    "stars",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "Review can not be less than 0 stars"
                            ),
                            django.core.validators.MaxValueValidator(
                                5, "Review can not be more than 5 stars"
                            ),
                        ]
                    ),
                ),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
    ]