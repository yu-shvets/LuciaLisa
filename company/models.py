from django.db import models


class ClientEmails(models.Model):

    class Meta(object):
        verbose_name = "Client's email"
        verbose_name_plural = "Client's emails"

    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.email)
