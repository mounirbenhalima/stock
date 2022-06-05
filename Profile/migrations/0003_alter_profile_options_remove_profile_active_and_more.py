# Generated by Django 4.0.4 on 2022-05-25 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_remove_point_user_remove_salary_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='active',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='company',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hiring_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rest_holiday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='self_transported',
        ),
    ]