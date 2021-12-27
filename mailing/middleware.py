import traceback

from django.http import JsonResponse, HttpResponse
from rest_framework.authtoken.models import Token

from mailing.service import create_mail_files


class Authorization:

    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        response = self._get_response(request)
        create_mail_files()
        return response

    def process_exception(self, request, exception):
        return JsonResponse({
            'success': False,
            'message': str(exception),
        }, status=417)
