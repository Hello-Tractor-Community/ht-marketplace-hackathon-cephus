# Generated by Django 5.1 on 2024-11-25 11:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Payment Amount')),
                ('ref', models.CharField(max_length=250, unique=True, verbose_name='Reference')),
                ('email', models.EmailField(max_length=250, verbose_name='Email Address')),
                ('verified', models.BooleanField(default=False, verbose_name='Verified Payment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='order.order', verbose_name='Order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]