from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Snippet


def get_snippet(func):
    def inner(request: Request, pk: int, *args, **kwargs):
        try:
            snippet = Snippet.objects.get(pk=pk)
            return func(request, snippet, *args, **kwargs)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return inner
