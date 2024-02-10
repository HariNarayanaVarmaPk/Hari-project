from django.conf import settings
from django.urls import  path
from . import views
from django.conf.urls.static import static
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)