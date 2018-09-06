from django.db import models


class Auth(models.Model):
    """認可"""
    authId = models.CharField('認可ID', max_length=255, unique=True)
    userId = models.CharField('ユーザID', max_length=255)
    regTs = models.DateTimeField('登録日時', auto_now_add=True)

    def __str__(self):
        return self.authId


class RefreshToken(models.Model):
    """リフレッシュトークン"""
    refreshTokenId = models.CharField('リフレッシュトークンID', max_length=255, unique=True)
    authId = models.CharField('認可ID', max_length=255)
    refreshToken = models.CharField('リフレッシュトークン', max_length=255)
    validTs = models.TimeField('有効期限')
    regTs = models.DateTimeField('登録日時', auto_now_add=True)

    def __str__(self):
        return self.refreshTokenId


class AccessToken(models.Model):
    """アクセストークン"""
    AccessTokenId = models.CharField('アクセストークンID', max_length=255, unique=True)
    refreshTokenId = models.CharField('リフレッシュトークンID', max_length=255)
    AccessToken = models.CharField('アクセストークン', max_length=255)
    validTs = models.TimeField('有効期限')
    regTs = models.DateTimeField('登録日時', auto_now_add=True)

    def __str__(self):
        return self.AccessTokenId


class User(models.Model):
    """ユーザ"""
    userId = models.CharField('ユーザID', max_length=255)
    password = models.CharField('パスワード', max_length=255)

    def __str__(self):
        return self.userId
