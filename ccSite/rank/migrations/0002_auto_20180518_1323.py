# Generated by Django 2.0.5 on 2018-05-18 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rulebook',
            old_name='votes',
            new_name='general_votes',
        ),
        migrations.RemoveField(
            model_name='rulebook',
            name='rulebook_text',
        ),
        migrations.AddField(
            model_name='rulebook',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='description_text',
            field=models.CharField(default='description', max_length=200),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='game_time_median',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='luck_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date modified'),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='num_players_max',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='num_players_min',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='recomended_age_max',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='recomended_age_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='skill_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='valor_hot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rulebook',
            name='valor_new',
            field=models.IntegerField(default=0),
        ),
    ]