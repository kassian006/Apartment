# Generated by Django 5.1.7 on 2025-03-25 09:14

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
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
                ('user_role', models.CharField(choices=[('agent', 'agent'), ('client', 'client'), ('owner', 'owner')], default='client', max_length=16)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_image/')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='owner_img')),
                ('about_owner', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_typ', models.CharField(choices=[('Apartment', 'Apartment'), ('Villa', 'Villa'), ('Townhouse', 'Townhouse'), ('Penthouse', 'Penthouse'), ('Whole Building', 'Whole Building')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(max_length=80)),
                ('active_listings', models.IntegerField(default=0)),
                ('experience_since', models.DateField()),
                ('image_company', models.ImageField(blank=True, null=True, upload_to='company_image/')),
                ('superagent', models.BooleanField(default=False)),
                ('social_agent', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Agent',
                'verbose_name_plural': 'Agent',
            },
            bases=('izde.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_home', models.CharField(choices=[('Rent', 'rent'), ('Buy', 'buy')], max_length=32)),
                ('house_name', models.CharField(max_length=80)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('home_image', models.ImageField(blank=True, null=True, upload_to='home_images/')),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('square', models.IntegerField()),
                ('aminities', multiselectfield.db.fields.MultiSelectField(choices=[('balcony', 'balcony'), ('microwave', 'microwave'), ('WiFi', 'WiFi'), ('Covered parking', 'covered parking'), ('TV', 'TV'), ('Central heating', 'central heating'), ('Washing_machine', 'washing machine'), ('Air-conditioner', 'air-conditioner'), ('Tableware', 'tableware'), ('Swimming pool', 'swimming pool'), ('Gym', 'gym'), ('Workspace', 'workspace'), ('Pet friendly', 'pet friendly')], max_length=140)),
                ('bathroom_type', models.CharField(choices=[('Combined', 'combined'), ('Separate', 'separate')], max_length=16)),
                ('parking_type', models.CharField(choices=[('Ground', 'ground'), ('Underground', 'underground'), ('No', 'no')], max_length=32)),
                ('number_room', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('floor', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11')], null=True)),
                ('series', models.CharField(choices=[('Elite', 'elite'), ('105', '105'), ('106', '106'), ('104', '104'), ('Individual project', 'Individual project')], max_length=32)),
                ('descriptions', models.TextField()),
                ('house_roules', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_home', to='izde.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_house', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_image', models.ImageField(upload_to='house_images/')),
                ('hom_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_house', to='izde.house')),
            ],
        ),
        migrations.CreateModel(
            name='HouseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_review', to=settings.AUTH_USER_MODEL)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_review', to='izde.house')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=32)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='izde.house')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('social_url', models.URLField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='SelectedWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=300)),
                ('url', models.URLField(blank=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_works', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resume_agents/')),
                ('status', models.CharField(choices=[('declined', 'Declined'), ('accepted', 'Accepted')], max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_resume', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=50)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby_name', models.CharField(max_length=50)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobbies', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('institution_name', models.CharField(max_length=200)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=50)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_areas', to='izde.agentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='AgentRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('text', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='izde.agentprofile')),
            ],
        ),
    ]
