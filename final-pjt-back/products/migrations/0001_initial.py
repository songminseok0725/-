# Generated by Django 4.2.4 on 2023-11-21 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('dcls_chrg_man', models.TextField()),
                ('homp_url', models.TextField()),
                ('cal_tel', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Deposite_baselist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_end_day', models.TextField(blank=True, null=True)),
                ('dcls_month', models.TextField()),
                ('dcls_strt_day', models.TextField()),
                ('etc_note', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_co_subm_day', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_deny', models.TextField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Saving_baselist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_end_day', models.TextField(blank=True, null=True)),
                ('dcls_month', models.TextField()),
                ('dcls_strt_day', models.TextField()),
                ('etc_note', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_co_subm_day', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_deny', models.TextField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Saving_optionlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate', models.FloatField(blank=True, null=True)),
                ('intr_rate2', models.FloatField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('rsrv_type', models.TextField()),
                ('rsrv_type_nm', models.TextField()),
                ('save_trm', models.TextField()),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.saving_baselist')),
            ],
        ),
        migrations.CreateModel(
            name='Deposite_optionlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate', models.FloatField(blank=True, null=True)),
                ('intr_rate2', models.FloatField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('save_trm', models.TextField()),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.deposite_baselist')),
            ],
        ),
    ]
