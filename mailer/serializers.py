from rest_framework.serializers import ModelSerializer
from .models import MailingDetails

class MailSerializer(ModelSerializer):

    class Meta:
        model = MailingDetails
        fields = [
            'subject',
            'body',
            'mail_to',
            'mail_from',
        ]