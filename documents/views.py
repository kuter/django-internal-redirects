from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import Document


def redirect_test(request, path):
    document = get_object_or_404(Document, document=path)
    if document.public or request.user.is_authenticated:
        response = HttpResponse()
        response['X-Accel-Redirect'] = '/protected-media/' + path
        return response
    else:
        raise PermissionDenied()
