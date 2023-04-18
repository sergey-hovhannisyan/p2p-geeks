# Generated by Django 4.2 on 2023-04-17 23:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_rename_user_id_skill_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="skill",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Skill 1", "C++"),
                    ("Skill 2", "Skill 2"),
                    ("Skill 3", "Skill 3"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="skill",
            name="skill_level",
            field=models.IntegerField(
                blank=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
    ]
