# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0042_updated_at_subawards'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryTransactionFedAcctView',
            fields=[
                ('duh', models.UUIDField(help_text='Deterministic Unique Hash', primary_key=True, serialize=False)),
                ('action_date', models.DateField()),
                ('fiscal_year', models.IntegerField()),
                ('type', models.TextField()),
                ('pulled_from', models.TextField()),
                ('federal_account_id', models.IntegerField()),
                ('treasury_account_id', models.IntegerField()),
                ('agency_identifier', models.TextField()),
                ('main_account_code', models.TextField()),
                ('account_title', models.TextField()),
                ('federal_account_display', models.TextField()),
                ('recipient_hash', models.UUIDField()),
                ('recipient_name', models.TextField()),
                ('recipient_unique_id', models.TextField()),
                ('parent_recipient_unique_id', models.TextField()),
                ('generated_pragmatic_obligation', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('federal_action_obligation', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('original_loan_subsidy_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('face_value_loan_guarantee', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('counts', models.IntegerField()),
            ],
            options={
                'db_table': 'summary_transaction_fed_acct_view',
                'managed': False,
            },
        ),
    ]