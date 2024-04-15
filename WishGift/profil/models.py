from django.conf import settings
from django.db import models


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="following",
                             on_delete=models.CASCADE)

    following_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                          related_name="followers",
                                          on_delete=models.CASCADE)

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