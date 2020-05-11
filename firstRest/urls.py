from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (articleList,
                    articleDetail,
                    ArticaleAPIView,
                    DetailView, GenericAPIView,
                    ArticleViewSet, ArticleGenericViewSet,
                    ArticleModelViewSet)

router = DefaultRouter()
router.register('articleSet', ArticleViewSet, basename='articleSet')
router.register('genericSet', ArticleGenericViewSet, basename='genericSet')
router.register('modelSet', ArticleModelViewSet, basename='modelSet')

urlpatterns = [
    path('', include(router.urls)),
    path('/<int:pk>/', include(router.urls)),
    path('', articleList, name="article"),
    path('<int:pk>/', articleDetail, name="detail"),
    path('articleAPI/', ArticaleAPIView.as_view()),
    path('detail/<int:id>/', DetailView.as_view()),
    path('generics/<int:id>/', GenericAPIView.as_view()),
]
