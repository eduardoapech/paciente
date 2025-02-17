# Generated by Django 5.1.6 on 2025-02-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pacientes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tarefas",
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
                ("tarefa", models.CharField(max_length=255)),
                ("instrucoes", models.TextField()),
                (
                    "frequencia",
                    models.CharField(
                        choices=[
                            ("D", "Diário"),
                            ("1S", "1 vez por semana"),
                            ("2S", "2 vezes por semana"),
                            ("3S", "3 vezes por semana"),
                            ("N", "Ao necessitar"),
                        ],
                        default="D",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
