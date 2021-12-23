from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from news.models import News
from news.serializers import NewsSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']
