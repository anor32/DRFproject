import os

from django.core.management import BaseCommand

from users.models import User, UserRoles


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin = User.objects.create(
            email="admin@web.top",
            first_name='admin',
            last_name='Adminov',
            role = UserRoles.MODERATOR,
            is_staff = True,
            is_superuser = True,
            is_active= True,
        )
        admin.set_password('qwerty')
        admin.save()
        print('Админ создан')


        moderator = User.objects.create(
            email="moderator@web.top",
            first_name='moderator',
            last_name='moderator',
            role=UserRoles.MODERATOR,
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )
        moderator.set_password('qwerty')
        moderator.save()
        print("Модератор создан")



        user = User.objects.create(
            email="user@web.top",
            first_name='user',
            last_name='userov',
            role=UserRoles.MEMBER,
            is_staff=False,
            is_superuser=False,
            is_active=False,
        )
        user.set_password('qwerty')
        user.save()
        print('Пользователь создан')