# Generated by Django 2.1.5 on 2019-04-03 16:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('penpalz_app', '0005_remove_message_prof_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='prof_of_lang', to='penpalz_app.Lang'),
        ),
        migrations.AlterField(
            model_name='prof',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
