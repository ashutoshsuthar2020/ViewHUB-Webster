# Generated by Django 4.1.2 on 2022-10-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_alter_upload_postid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="upload",
            name="postId",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]