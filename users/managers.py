from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Кастомный менеджер для модели User"""

    def create_user(
        self, email: str, username: str, password: str = None, **extra_fields
    ):
        """Создает и возвращает пользователя."""

        if not email:
            raise ValueError("Пользователь должен иметь электронную почту.")

        if not username:
            raise ValueError("Пользователь должен иметь имя пользователя.")

        if not password:
            raise ValueError("Пользователь должен иметь пароль.")

        user = self.model(
            username=username, email=self.normalize_email(email=email), **extra_fields
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self, email: str, username: str, password: str, **extra_fields
    ):
        """Создает и возвращает пользователя с привилегиями суперпользователя."""
        if password is None:
            raise TypeError("Суперпользователь должен иметь пароль.")

        if username is None:
            raise TypeError("Суперпользователь должен иметь имя пользователя.")

        if email is None:
            raise ValueError("Суперпользователь должен иметь электронную почту.")

        user = self.create_user(
            email=email, username=username, password=password, **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
