# Generated by Django 3.0.3 on 2020-09-26 20:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('patronymic', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15, verbose_name='Гос. номер')),
                ('brand', models.CharField(max_length=30, verbose_name='Марка')),
                ('model', models.CharField(max_length=30, verbose_name='Модель')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('tech_passport', models.CharField(max_length=20, unique=True, verbose_name='Тех. паспорт')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autos', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Мастерская',
                'verbose_name_plural': 'Мастерские',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_beg', models.DateField(verbose_name='Дата начала')),
                ('date_end', models.DateField(blank=True, verbose_name='Дата завершения')),
                ('description', models.TextField(verbose_name='Описание работ')),
                ('price', models.FloatField(blank=True, verbose_name='Стоимость')),
                ('auto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auto_works', to='django_app.Auto', verbose_name='Автомобиль')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_works', to='django_app.Employee', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Ремонтная работа',
                'verbose_name_plural': 'Ремонтные работы',
            },
        ),
        migrations.CreateModel(
            name='Served_brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(db_index=True, max_length=30, verbose_name='Обслуживаемая марка')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='django_app.Workshop', verbose_name='Мастерская')),
            ],
            options={
                'verbose_name': 'Обслуживаемая марка',
                'verbose_name_plural': 'Обслуживаемые марки',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='autos',
            field=models.ManyToManyField(related_name='employees', through='django_app.Work', to='django_app.Auto', verbose_name='Ремонтные работы'),
        ),
        migrations.AddField(
            model_name='employee',
            name='workshop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_app.Workshop', verbose_name='Мастерская'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата записи')),
                ('status', models.CharField(choices=[('cons', 'В рассмотрении'), ('conf', 'Подтверждено'), ('refs', 'Отклонено')], max_length=4)),
                ('date_init', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications_auto', to='django_app.Auto', verbose_name='Автомобиль')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications_workshop', to='django_app.Workshop', verbose_name='Мастерская')),
            ],
            options={
                'verbose_name': 'Заявка на ремонт',
                'verbose_name_plural': 'Заявки на ремонт',
            },
        ),
    ]
