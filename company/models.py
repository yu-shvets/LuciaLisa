from django.db import models
from products.models import CommonInfo


class ClientEmails(models.Model):

    class Meta(object):
        verbose_name = "Client's email"
        verbose_name_plural = "Client's emails"

    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.email)


class News(CommonInfo):

    class Meta(object):
        verbose_name = "News"
        verbose_name_plural = "News"

    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return "{}".format(self.created)