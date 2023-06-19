from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, renderers
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This view set automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request: Request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view set automatically provides 'list' and 'retrieve' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
