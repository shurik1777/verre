from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    class Meta:
        # db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.core.mail import send_mail
# from django.db import models
# from django.utils import timezone
# from django.core.validators import FileExtensionValidator
# from PIL import Image
#
# # from .validators import validate_filesize_10_mb
# from users.managers import UserManager
#
# class User(AbstractBaseUser, PermissionsMixin):
#     """Модель пользователя"""
#
#     username = models.CharField(
#         max_length=32,
#         verbose_name="Имя пользователя",
#         null=False,
#         blank=False,
#         unique=True,
#     )
#     password = models.CharField(
#         max_length=32, verbose_name="Пароль", null=False, blank=False
#     )
#     first_name = models.CharField(
#         max_length=150, verbose_name="Имя", null=True, blank=True
#     )
#     last_name = models.CharField(
#         max_length=150, verbose_name="Фамилия", null=True, blank=True
#     )
#     email = models.EmailField(
#         verbose_name="Электронная почта", null=False, blank=False, unique=True
#     )
#
#     is_active = models.BooleanField(verbose_name="Активен", default=False)
#
#     is_superuser = models.BooleanField(verbose_name="Суперпользователь", default=False)
#
#     is_staff = models.BooleanField(verbose_name="Сотрудник", default=False)
#
#     date_joined = models.DateTimeField(
#         verbose_name="Дата регистрации", default=timezone.now
#     )
#
#     updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
#     profile_picture = models.ImageField(
#         verbose_name="Аватар_100",
#         upload_to="avatars/%Y%M%D",
#         default="default_profile_images/default_100.png",
#         validators=[
#             FileExtensionValidator(
#                 allowed_extensions=[
#                     "jpg",
#                     "png",
#                     "jpeg",
#                     "webp",
#                     "bmp",
#                     "gif",
#                     "tiff",
#                     "tif",
#                     "svg",
#                     "heic",
#                 ]
#             ),
#             # validate_filesize_10_mb,
#         ],
#         null=True,
#         blank=True,
#     )
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]
#     objects = UserManager()
#
#     class Meta:
#         app_label = "user_app"
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
#
#     def __str__(self):
#         return self.username
#
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         """Метод отправки электронной почты пользователю"""
#         send_mail(subject, message, from_email, [self.email], **kwargs)
#
#     def save(self, *args, **kwargs):
#         """
#         Переопределение метода save
#         с учетом сохранения фото профиля
#         100 х 100
#         """
#         super(User, self).save(*args, **kwargs)
#
#         if self.profile_picture != "default_profile_images/default_100.png":
#             img = Image.open(self.profile_picture.path)
#             img.thumbnail((100, 100))
#             img.save(self.profile_picture.path)
