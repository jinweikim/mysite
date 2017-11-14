from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import AuthorViewSet,CategoryViewSet,TrainViewSet
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.log_in,name='login'),
    url(r'^logout/$',views.log_out,name='logout'),
    url(r'^(?P<article_id>[0-9]+)/comment/$',views.comment,name='comment'),
    url(r'^(?P<article_id>[0-9]+)/$',views.article,name='article'),
    url(r'^tag/(?P<tag_id>\d+)$',views.TagView.as_view(),name='tag'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = routers.DefaultRouter()
router.register(r'author',AuthorViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'train',TrainViewSet)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)