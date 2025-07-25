# Generated by Django 5.2.4 on 2025-07-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('tech', 'Technology'), ('life', 'Lifestyle'), ('edu', 'Education'), ('news', 'News'), ('health', 'Health'), ('travel', 'Travel'), ('food', 'Food'), ('sports', 'Sports'), ('finance', 'Finance'), ('ent', 'Entertainment')], default='tech', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
