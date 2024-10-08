# Generated by Django 4.2.13 on 2024-08-13 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_flight_approval_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('flight_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FlightPassenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_baggage', models.BooleanField(default=False)),
                ('flight_count', models.IntegerField(default=0)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.passenger')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='passengers',
            field=models.ManyToManyField(through='flights.FlightPassenger', to='flights.passenger'),
        ),
    ]
