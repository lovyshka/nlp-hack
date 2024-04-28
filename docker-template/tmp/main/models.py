from django.db import models
from django.contrib.auth.models import AbstractUser

import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

class CustomUser(AbstractUser):
    telegram_chat_id = models.PositiveBigIntegerField(
        verbose_name="ID пользователя",
        null=True,
    )

    verified_usr = models.BooleanField(
        verbose_name="Верификация пользователя",
        default=False,
    )

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"