from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
import pkg_resources
import coreapi

# View for the homepage
from ipo_app.views import IPODetail 
from ipo_app import views

def home_view(request):
    return HttpResponse("<h1>Welcome to the IPO Information App</h1>")

# URL patterns
urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('api/ipo-statistics/', views.get_ipo_data, name='ipo-data'),
        path('', views.home, name='home'),
    path('api/ipo-statistics/', views.get_ipo_data, name='ipo-statistics'),
    path('api/ipo-details/<int:pk>/', IPODetail.as_view(), name='ipo-details'),
    path('api/download-links/', views.download_links, name='download-links'),
    
    
    path('', home_view, name='home'),  # Home page
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('ipo_app.urls', namespace='ipo_app')),  # Include API routes
    path('api/docs/', include_docs_urls(title="IPO API Documentation")),  # API docs
    path('api/schema/', get_schema_view(title="IPO API Schema"), name='api-schema'),  # API schema
]

# Static and media file handling
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


