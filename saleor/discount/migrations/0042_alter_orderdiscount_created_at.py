# Generated by Django 3.2.13 on 2022-05-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("discount", "0041_fulfill_orderdiscount_token_created_at_old_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdiscount",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
