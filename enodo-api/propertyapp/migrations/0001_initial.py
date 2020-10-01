# Generated by Django 2.2 on 2020-10-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_address', models.TextField(blank=True, db_column='Full Address', null=True)),
                ('longitude', models.FloatField(blank=True, db_column='Longitude', null=True)),
                ('latitude', models.FloatField(blank=True, db_column='Latitude', null=True)),
                ('zip', models.IntegerField(blank=True, db_column='Zip', null=True)),
                ('rec_type', models.TextField(blank=True, db_column='REC_TYPE', null=True)),
                ('pin', models.IntegerField(blank=True, db_column='PIN', null=True)),
                ('ovacls', models.IntegerField(blank=True, db_column='OVACLS', null=True)),
                ('class_description', models.TextField(blank=True, db_column='CLASS_DESCRIPTION', null=True)),
                ('current_land', models.IntegerField(blank=True, db_column='CURRENT_LAND', null=True)),
                ('current_building', models.IntegerField(blank=True, db_column='CURRENT_BUILDING', null=True)),
                ('current_total', models.IntegerField(blank=True, db_column='CURRENT_TOTAL', null=True)),
                ('estimated_market_value', models.IntegerField(blank=True, db_column='ESTIMATED_MARKET_VALUE', null=True)),
                ('prior_land', models.IntegerField(blank=True, db_column='PRIOR_LAND', null=True)),
                ('prior_building', models.IntegerField(blank=True, db_column='PRIOR_BUILDING', null=True)),
                ('prior_total', models.IntegerField(blank=True, db_column='PRIOR_TOTAL', null=True)),
                ('pprior_land', models.IntegerField(blank=True, db_column='PPRIOR_LAND', null=True)),
                ('pprior_building', models.IntegerField(blank=True, db_column='PPRIOR_BUILDING', null=True)),
                ('pprior_total', models.IntegerField(blank=True, db_column='PPRIOR_TOTAL', null=True)),
                ('pprior_year', models.IntegerField(blank=True, db_column='PPRIOR_YEAR', null=True)),
                ('town', models.IntegerField(blank=True, db_column='TOWN', null=True)),
                ('volume', models.IntegerField(blank=True, db_column='VOLUME', null=True)),
                ('loc', models.TextField(blank=True, db_column='LOC', null=True)),
                ('tax_code', models.IntegerField(blank=True, db_column='TAX_CODE', null=True)),
                ('neighborhood', models.IntegerField(blank=True, db_column='NEIGHBORHOOD', null=True)),
                ('houseno', models.IntegerField(blank=True, db_column='HOUSENO', null=True)),
                ('dir', models.TextField(blank=True, db_column='DIR', null=True)),
                ('street', models.TextField(blank=True, db_column='STREET', null=True)),
                ('suffix', models.TextField(blank=True, db_column='SUFFIX', null=True)),
                ('apt', models.TextField(blank=True, db_column='APT', null=True)),
                ('city', models.TextField(blank=True, db_column='CITY', null=True)),
                ('res_type', models.TextField(blank=True, db_column='RES_TYPE', null=True)),
                ('bldg_use', models.TextField(blank=True, db_column='BLDG_USE', null=True)),
                ('apt_desc', models.TextField(blank=True, db_column='APT_DESC', null=True)),
                ('comm_units', models.TextField(blank=True, db_column='COMM_UNITS', null=True)),
                ('ext_desc', models.TextField(blank=True, db_column='EXT_DESC', null=True)),
                ('full_bath', models.IntegerField(blank=True, db_column='FULL_BATH', null=True)),
                ('half_bath', models.IntegerField(blank=True, db_column='HALF_BATH', null=True)),
                ('bsmt_desc', models.TextField(blank=True, db_column='BSMT_DESC', null=True)),
                ('attic_desc', models.TextField(blank=True, db_column='ATTIC_DESC', null=True)),
                ('ac', models.IntegerField(blank=True, db_column='AC', null=True)),
                ('fireplace', models.IntegerField(blank=True, db_column='FIREPLACE', null=True)),
                ('gar_desc', models.TextField(blank=True, db_column='GAR_DESC', null=True)),
                ('age', models.IntegerField(blank=True, db_column='AGE', null=True)),
                ('building_sq_ft', models.IntegerField(blank=True, db_column='BUILDING_SQ_FT', null=True)),
                ('land_sq_ft', models.IntegerField(blank=True, db_column='LAND_SQ_FT', null=True)),
                ('bldg_sf', models.TextField(blank=True, db_column='BLDG_SF', null=True)),
                ('units_tot', models.TextField(blank=True, db_column='UNITS_TOT', null=True)),
                ('multi_sale', models.IntegerField(blank=True, db_column='MULTI_SALE', null=True)),
                ('deed_type', models.IntegerField(blank=True, db_column='DEED_TYPE', null=True)),
                ('sale_date', models.TextField(blank=True, db_column='SALE_DATE', null=True)),
                ('sale_amount', models.IntegerField(blank=True, db_column='SALE_AMOUNT', null=True)),
                ('appcnt', models.IntegerField(blank=True, db_column='APPCNT', null=True)),
                ('appeal_a', models.IntegerField(blank=True, db_column='APPEAL_A', null=True)),
                ('appeal_a_status', models.TextField(blank=True, db_column='APPEAL_A_STATUS', null=True)),
                ('appeal_a_result', models.TextField(blank=True, db_column='APPEAL_A_RESULT', null=True)),
                ('appeal_a_reason', models.IntegerField(blank=True, db_column='APPEAL_A_REASON', null=True)),
                ('appeal_a_pin_result', models.TextField(blank=True, db_column='APPEAL_A_PIN_RESULT', null=True)),
                ('appeal_a_propav', models.IntegerField(blank=True, db_column='APPEAL_A_PROPAV', null=True)),
                ('appeal_a_currav', models.IntegerField(blank=True, db_column='APPEAL_A_CURRAV', null=True)),
                ('appeal_a_resltdate', models.TextField(blank=True, db_column='APPEAL_A_RESLTDATE', null=True)),
            ],
            options={
                'db_table': 'PropertyInfo',
                'managed': False,
            },
        ),
    ]