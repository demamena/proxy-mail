from rest_framework.response import Response
from rest_framework.views import APIView

from mailing.models import MailingUser
from mailing.service import create_mail_user, create_mail_files


class CreateMailUser(APIView):

    def post(self, request):
        create_mail_user(request.GET.get('email'), request.GET.get('status'))
        return Response({'success': True})


class DeleteMailUser(APIView):

    def delete(self, request):
        MailingUser.objects.get(email=request.GET.get('email')).delete()
        return Response({'success': True})


class ChangeMailUser(APIView):

    def put(self, request):
        user = MailingUser.objects.get(email=request.GET.get('old_email'))
        user.email = request.GET.get('new_email')
        user.save()
        return Response({'success': True})


