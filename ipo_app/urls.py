from django.urls import path
from .views import IPOList, IPODetail, IPOStatistics
app_name = 'ipo_app'


urlpatterns = [
    path('ipo-list/', IPOList.as_view(), name='ipo-list'),
    path('ipo-detail/<int:pk>/', IPODetail.as_view(), name='ipo-detail'),
    path('ipo-statistics/', IPOStatistics.as_view(), name='ipo-statistics'),  # New endpoint
]
