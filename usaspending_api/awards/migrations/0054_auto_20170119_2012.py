# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-19 20:12
from __future__ import unicode_literals

from django.db import migrations, models

from django.db.models import Case, F, Value, When


def update_award_actions(apps, schema_editor):
    # Use procurement model at time of migration
    Procurement = apps.get_model("awards", "Procurement")
    # set new description field equal to value of current award_description
    Procurement.objects.all().update(description=F("award_description"))
    # set new type field equal to value of contract_award_type
    Procurement.objects.all().update(type=F("contract_award_type"))
    # set new type description field =
    Procurement.objects.all().update(type_description=(Case(
        When(contract_award_type='A', then=Value('BPA Call')),
        When(contract_award_type='B', then=Value('Purchase Order')),
        When(contract_award_type='C', then=Value('Delivery Order')),
        When(contract_award_type='D', then=Value('Definitive Contract')),
        default=Value('Unknown Type')
    )))

    FinancialAssistanceAward = apps.get_model("awards", "FinancialAssistanceAward")
    # set new description field equal to value of current award_description
    FinancialAssistanceAward.objects.all().update(description=F("award_description"))
    # set new type field equal to value of contract_award_type
    FinancialAssistanceAward.objects.all().update(type=F("assistance_type"))
    # set new type description field =
    FinancialAssistanceAward.objects.all().update(type_description=(Case(
        When(assistance_type='02', then=Value('Block Grant')),
        When(assistance_type='03', then=Value('Formula Grant')),
        When(assistance_type='04', then=Value('Project Grant')),
        When(assistance_type='05', then=Value('Cooperative Agreement')),
        When(assistance_type='06', then=Value('Direct Payment for Specified Use')),
        When(assistance_type='07', then=Value('Direct Loan')),
        When(assistance_type='08', then=Value('Guaranteed/Insured Loan')),
        When(assistance_type='09', then=Value('Insurance')),
        When(assistance_type='10', then=Value('Direct Payment unrestricted')),
        When(assistance_type='11', then=Value('Other')),
        default=Value('Unknown Type')
    )))


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0053_auto_20170111_2100'),
    ]

    operations = [

        # add and rename some fields
        migrations.AddField(
            model_name='financialassistanceaward',
            name='description',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='financialassistanceaward',
            name='period_of_performance_current_end_date',
            field=models.DateField(max_length=10, null=True, verbose_name='Period of Performance Current End Date'),
        ),
        migrations.AddField(
            model_name='financialassistanceaward',
            name='period_of_performance_start_date',
            field=models.DateField(max_length=10, null=True, verbose_name='Period of Performance Start Date'),
        ),
        migrations.AddField(
            model_name='financialassistanceaward',
            name='type',
            field=models.CharField(choices=[('U', 'Unknown Type'), ('02', 'Block Grant'), ('03', 'Formula Grant'), ('04', 'Project Grant'), ('05', 'Cooperative Agreement'), ('06', 'Direct Payment for Specified Use'), ('07', 'Direct Loan'), ('08', 'Guaranteed/Insured Loan'), ('09', 'Insurance'), ('10', 'Direct Payment unrestricted'), ('11', 'Other'), ('A', 'BPA Call'), ('B', 'Purchase Order'), ('C', 'Delivery Order'), ('D', 'Definitive Contract')], default='U', max_length=5, null=True, verbose_name='Action Type'),
        ),
        migrations.AddField(
            model_name='financialassistanceaward',
            name='type_description',
            field=models.CharField(default='Unknown Type', max_length=50, null=True, verbose_name='Action Type Description'),
        ),
        migrations.AddField(
            model_name='procurement',
            name='description',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='procurement',
            name='period_of_performance_current_end_date',
            field=models.DateField(max_length=10, null=True, verbose_name='Period of Performance Current End Date'),
        ),
        migrations.AddField(
            model_name='procurement',
            name='period_of_performance_start_date',
            field=models.DateField(max_length=10, null=True, verbose_name='Period of Performance Start Date'),
        ),
        migrations.AddField(
            model_name='procurement',
            name='type',
            field=models.CharField(choices=[('U', 'Unknown Type'), ('02', 'Block Grant'), ('03', 'Formula Grant'), ('04', 'Project Grant'), ('05', 'Cooperative Agreement'), ('06', 'Direct Payment for Specified Use'), ('07', 'Direct Loan'), ('08', 'Guaranteed/Insured Loan'), ('09', 'Insurance'), ('10', 'Direct Payment unrestricted'), ('11', 'Other'), ('A', 'BPA Call'), ('B', 'Purchase Order'), ('C', 'Delivery Order'), ('D', 'Definitive Contract')], default='U', max_length=5, null=True, verbose_name='Action Type'),
        ),
        migrations.AddField(
            model_name='procurement',
            name='type_description',
            field=models.CharField(default='Unknown Type', max_length=50, null=True, verbose_name='Action Type Description'),
        ),
        migrations.AlterField(
            model_name='award',
            name='type',
            field=models.CharField(choices=[('U', 'Unknown Type'), ('02', 'Block Grant'), ('03', 'Formula Grant'), ('04', 'Project Grant'), ('05', 'Cooperative Agreement'), ('06', 'Direct Payment for Specified Use'), ('07', 'Direct Loan'), ('08', 'Guaranteed/Insured Loan'), ('09', 'Insurance'), ('10', 'Direct Payment unrestricted'), ('11', 'Other'), ('A', 'BPA Call'), ('B', 'Purchase Order'), ('C', 'Delivery Order'), ('D', 'Definitive Contract')], default='U', max_length=5, null=True, verbose_name='Award Type'),
        ),
        migrations.AlterField(
            model_name='award',
            name='type_description',
            field=models.CharField(default='Unknown Type', max_length=50, null=True, verbose_name='Award Type Description'),
        ),

        # populate newly-added fields using data in old fields
        migrations.RunPython(update_award_actions, reverse_code=migrations.RunPython.noop),

        # remove old fields
        migrations.RemoveField(
            model_name='financialassistanceaward',
            name='assistance_type',
        ),
        migrations.RemoveField(
            model_name='financialassistanceaward',
            name='award_description',
        ),
        migrations.RemoveField(
            model_name='procurement',
            name='award_description',
        ),
        migrations.RemoveField(
            model_name='procurement',
            name='contract_award_type',
        ),
    ]
