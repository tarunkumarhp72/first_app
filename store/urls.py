from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views 
urlpatterns = [  

    path('', views.dashboard_view, name='dashboard'),  
    path('park/', views.list_parks_view, name='list_parks_view'),
    path('park/create/', views.create_park_view, name='create_park_view'),
    path('park/edit/<int:id>/', views.edit_park_view, name='edit_park_view'),
    path('park/delete/<int:id>/', views.delete_park_view, name='delete_park_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)