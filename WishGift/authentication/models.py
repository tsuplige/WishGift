from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings


class User(AbstractUser):

    def follow(self, followed_user):
        UserFollows.follow(self, followed_user)

    def unfollow(self, followed_user):
        UserFollows.unfollow(self, followed_user)


class UserFollows(models.Model):
    user = models.ForeignKey("User", related_name="following")

    following_user_id = models.ForeignKey("User", related_name="followers")

    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def follow(cls, user, followed_user):
        if not cls.objects.filter(user=user,
                                  followed_user=followed_user).exists():
            cls.objects.create(user=user, followed_user=followed_user)

    @classmethod
    def unfollow(cls, user, followed_user):
        cls.objects.filter(user=user, followed_user=followed_user).delete()

    def __str__(self):
        return f'{self.user} follows {self.followed_user}'
