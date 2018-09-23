from django.db import models

# Create your models here.
class Message(models.Model):
    """メッセージ"""
    message = models.CharField('メッセージ', max_length=255)

    def str(self):
        return self.message