# Generated by Django 4.1.3 on 2022-11-28 11:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('forget_password_token', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(default='', max_length=100)),
                ('blog_name', models.CharField(default='', max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='change_password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_password', models.CharField(max_length=500)),
                ('confirm_password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('cid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(default='', max_length=100)),
                ('tag_name', models.CharField(default='', max_length=100)),
                ('post_header', models.CharField(default='', max_length=500)),
                ('post_content', models.CharField(default='', max_length=500)),
                ('images', models.ImageField(blank=True, upload_to='images/')),
                ('document', models.FileField(blank=True, upload_to='File/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.blog')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('workad_at', models.CharField(max_length=100)),
                ('Studied_at', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('linkedin', models.URLField(max_length=500)),
                ('twitter', models.URLField(max_length=500)),
                ('instagram', models.URLField(max_length=500)),
                ('facebook', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('rid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('Comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='accounts.comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile_Pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='accounts.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='accounts.post'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.profile_pic'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
