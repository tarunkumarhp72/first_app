from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [  
    path('', views.dashboard_view, name='dashboard'),  
    path('park/', views.list_parks_view, name='list_parks_view'),
    path('park/create/', views.create_park_view, name='create_park_view'),
    path('park/edit/<int:id>/', views.edit_park_view, name='edit_park_view'),
    path('park/delete/<int:id>/', views.delete_park_view, name='delete_park_view'),
    
    path('trail/', views.TrailListView.as_view(), name='trail_list'),
    path('trail/create/', views.TrailCreateView.as_view(), name='trail_create'),
    path('trail/edit/<int:pk>/', views.TrailEditView.as_view(), name='trail_edit'),
    path('trail/delete/<int:pk>/', views.TrailDeleteView.as_view(), name='trail_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
