# Generated by Django 2.2.16 on 2020-10-30 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=255, verbose_name='порода')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255, verbose_name='окрас')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255, verbose_name='административный округ')),
            ],
        ),
        migrations.CreateModel(
            name='Ears',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ears', models.CharField(max_length=255, verbose_name='уши')),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255, verbose_name='вид')),
            ],
        ),
        migrations.CreateModel(
            name='Operating_organizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Эксплуатирующие организации')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=255, verbose_name='карточка учета животного №')),
                ('age', models.IntegerField(verbose_name='возраст, год')),
                ('weight', models.IntegerField(verbose_name='вес, кг')),
                ('name', models.CharField(max_length=255, verbose_name='кличка')),
                ('special_signs', models.CharField(max_length=255, verbose_name='особые приметы')),
                ('aviary', models.IntegerField(verbose_name='Вольер №')),
                ('identification_mark', models.BigIntegerField(null=True, verbose_name='идентификационная метка')),
                ('sterilization_date', models.CharField(max_length=255, null=True, verbose_name='дата стерилизации')),
                ('name_veterinarian', models.CharField(max_length=255, null=True, verbose_name='ф.и.о. ветеринарного врача')),
                ('socialized', models.BooleanField(default=False, verbose_name='Социализировано (да/нет)')),
                ('work_order', models.CharField(max_length=255, null=True, verbose_name='заказ-наряд / акт о поступлении животного №')),
                ('work_order_date', models.DateField(null=True, verbose_name='заказ-наряд дата/ акт о поступлении животного, дата')),
                ('catch_report', models.CharField(max_length=255, null=True, verbose_name='акт отлова №')),
                ('catching_address', models.CharField(max_length=255, null=True, verbose_name='адрес места отлова')),
                ('entity', models.CharField(max_length=255, null=True, verbose_name='юридическое лицо ')),
                ('name_guardians', models.CharField(max_length=255, null=True, verbose_name='ф.и.о. опекунов')),
                ('natural_person_name', models.CharField(max_length=255, null=True, verbose_name='физическое лицо ф.и.о.')),
                ('date_to_shelter', models.CharField(max_length=255, null=True, verbose_name='дата поступления в приют')),
                ('act_no', models.CharField(max_length=255, null=True, verbose_name='акт №')),
                ('date_leaving_shelter', models.CharField(max_length=255, null=True, verbose_name='дата выбытия из приюта')),
                ('act_retirement', models.CharField(max_length=255, null=True, verbose_name='акт/договор №')),
                ('name_leader_shelter', models.CharField(max_length=255, verbose_name='ф.и.о. руководителя приюта')),
                ('name_care_worker', models.CharField(max_length=255, verbose_name='ф.и.о. сотрудника по уходу за животным')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Breed')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Color')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test.District')),
                ('ears', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Ears')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Kind')),
                ('operating_organizations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Operating_organizations')),
            ],
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Оф. Краткое наименование префектуры')),
            ],
        ),
        migrations.CreateModel(
            name='Reason_death',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_death', models.CharField(max_length=255, verbose_name='причина смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Reason_euthanasia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_euthanasia', models.CharField(max_length=255, verbose_name='причина эвтаназии')),
            ],
        ),
        migrations.CreateModel(
            name='Reason_retirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_retirement', models.CharField(max_length=255, verbose_name='причина выбытия')),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=255, verbose_name='пол')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255, verbose_name='размер')),
            ],
        ),
        migrations.CreateModel(
            name='Tail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tail', models.CharField(max_length=255, verbose_name='хвост')),
            ],
        ),
        migrations.CreateModel(
            name='Wool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wool', models.CharField(max_length=255, verbose_name='шерсть')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name='№ п/п')),
                ('date', models.DateField(verbose_name='дата')),
                ('type_vaccine', models.CharField(max_length=255, verbose_name='вид вакцины')),
                ('series', models.CharField(max_length=255, verbose_name='№ серии')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Оф. Краткое наименование приюта')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес приюта')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='Телефон приюта')),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Prefecture')),
            ],
        ),
        migrations.CreateModel(
            name='Processing_parasites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name='№ п/п')),
                ('date', models.DateField(verbose_name='дата')),
                ('drug_name', models.CharField(max_length=255, verbose_name='название препарата')),
                ('dose', models.CharField(max_length=255, verbose_name='доза')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='reason_death',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test.Reason_death'),
        ),
        migrations.AddField(
            model_name='pet',
            name='reason_euthanasia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test.Reason_euthanasia'),
        ),
        migrations.AddField(
            model_name='pet',
            name='reason_retirement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test.Reason_retirement'),
        ),
        migrations.AddField(
            model_name='pet',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Sex'),
        ),
        migrations.AddField(
            model_name='pet',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Shelter'),
        ),
        migrations.AddField(
            model_name='pet',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Size'),
        ),
        migrations.AddField(
            model_name='pet',
            name='tail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Tail'),
        ),
        migrations.AddField(
            model_name='pet',
            name='wool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Wool'),
        ),
        migrations.CreateModel(
            name='Health_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата')),
                ('anamnesis', models.CharField(max_length=255, verbose_name='анамнез')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Pet')),
            ],
        ),
    ]
