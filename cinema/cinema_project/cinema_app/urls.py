from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.view, name='view'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add, name='add'),
    path('profile/view', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('cinema/update/<int:pk>/', views.update_cinema, name='update_cinema'), # type: ignore
    path('cinema/delete/<int:pk>/', views.delete_cinema, name='delete_cinema'), # type: ignore
    path('search/', views.search_by_category, name='search_by_category'),
    path('cinema/<int:cinema_id>/rate/', views.rate_movie, name='rate_movie'),
    path('cinema/<int:cinema_id>/comment/', views.comment_movie, name='comment_movie')

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)