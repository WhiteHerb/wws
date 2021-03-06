# Generated by Django 3.2.6 on 2021-09-16 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schoolgroup',
            fields=[
                ('schoolnameset', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gradegroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_count', models.IntegerField(default=0)),
                ('subjects', models.CharField(default='', max_length=100)),
                ('gradeset', models.IntegerField(default=0)),
                ('school', models.ForeignKey(db_column='school_id', default='', on_delete=django.db.models.deletion.CASCADE, related_name='school', to='accounts.schoolgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=80, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30)),
                ('stu_ID', models.CharField(max_length=5, unique=True)),
                ('sub_res', models.JSONField(default={})),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('grade', models.ForeignKey(db_column='grade_id', on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='accounts.gradegroup')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('schoolname', models.ForeignKey(db_column='schoolname_id', on_delete=django.db.models.deletion.CASCADE, related_name='schoolname', to='accounts.schoolgroup')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
