# Generated by Django 4.2 on 2023-08-24 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import health_app.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health_app', '0006_alter_diet_id_alter_diets_id_alter_emotion_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='blood_group',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact_no',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='height_cm',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default=health_app.models.default_profile_image_path, null=True, upload_to='profile_images/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='weight_kg',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.CreateModel(
            name='HealthReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('calorie_intake', models.PositiveIntegerField(default=0)),
                ('sleep_duration_minutes', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
