# Generated by Django 4.1.3 on 2022-12-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0017_post_bid_price_user_watched_list_alter_comment_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="closed", field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_artist",
            field=models.BooleanField(default=False),
        ),
    ]