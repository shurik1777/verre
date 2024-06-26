from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    class Meta:
        # db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
