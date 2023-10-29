# Generated by Django 4.2.6 on 2023-10-29 13:49

from django.db import migrations


def update_invalid_data(apps, schema_editor):
    MyModel = apps.get_model("bug", "Bug")
    invalid_to_valid = {
        "bug_type": {
            "New feature": "FEAT",
            "Error": "ERR",
        },
        "status": {
            "In progress": "WIP",
            "Under testing": "TEST",
        }
    }
    for field, choices in invalid_to_valid.items():
        for invalid, valid in choices.items():
            MyModel.objects.filter(**{field: invalid}).update(**{field: valid})


class Migration(migrations.Migration):

    dependencies = [
        ("bug", "0004_alter_bug_bug_type_alter_bug_description_and_more"),
    ]

    operations = [
        migrations.RunPython(update_invalid_data),
    ]