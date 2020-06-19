from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class MailingDetails(models.Model):
    subject = models.CharField(_("Title of the mail"), max_length=500)
    body = models.TextField(_("message content"))
    mail_to = models.EmailField(_("Recipient"))
    mail_from = models.EmailField(_("Sender"))
    timestamp = models.DateTimeField(auto_now_add=True)
    