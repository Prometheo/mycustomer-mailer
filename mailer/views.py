from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import MailSerializer
from .models import MailingDetails
from django.core.mail import send_mail

# Create your views here.
class MailListView(generics.ListCreateAPIView):
    queryset = MailingDetails.objects.all()
    serializer_class = MailSerializer

    def create(self, request, *args, **kwargs):
        try:
            send_mail(request.data['subject'], request.data['body'], 'olaoyejnr@gmail.com', request.data['mail_to'], fail_silently=False)
            data = {
                'message':'email successfully sent.',
                'status': status.HTTP_201_CREATED
            }
            if len(request.data['mail_to']) < 2:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
            else:
                for dif_mail in request.data['mail_to']:
                    serializer = self.get_serializer(data = {
                        'subject': request.data['subject'],
                        'body': request.data['body'],
                        'mail_to': dif_mail,
                        'mail_from': 'olaoyejnr@gmail.com'  
                    })
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                return Response(data)

        except Exception:
            data = {
                'error':'email not sent, please try again.'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        
        
            
        

       
# class MailCreateView(generics.CreateAPIView):
#     queryset = MailingDetails.objects.all()
#     serializer_class = MailSerializer

