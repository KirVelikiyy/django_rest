from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Snippet
from .serializers import SnippetSerializer
from .decorators import get_snippet


class SnippetList(APIView):
    """
    List all code snippets, or create a new snippet
    """
    @staticmethod
    def get(request: Request, **kwargs):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request: Request, **kwargs):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnipperDetail(APIView):
    """
    Retrieve, update or delete a code snippet
    """
    @staticmethod
    @get_snippet
    def get(request: Request, snippet: Snippet, **kwargs):
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    @staticmethod
    @get_snippet
    def put(request: Request, snippet: Snippet, **kwargs):
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @get_snippet
    def delete(request: Request, snippet: Snippet, **kwargs):
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
