from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IPO
from .serializers import IPOSerializer
from django.db.models import Count, Q
import coreapi
import pkg_resources
# IPO List View (No Changes)
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def get_ipo_data(request):
    data = {
        "total_ipo": 10,
        "ipo_in_gain": 7,
        "ipo_in_loss": 3,
    }
    return JsonResponse(data)

class IPOList(APIView):
    def get(self, request):
        ipo_data = IPO.objects.all()
        serializer = IPOSerializer(ipo_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


def download_links(request):
    # Example data for download links
    data = {
        "link1": "http://example.com/download1",
        "link2": "http://example.com/download2",
    }
    return JsonResponse(data)

# IPO Detail View (No Changes)
class IPODetail(APIView):
    def get(self, request, pk):
        try:
            ipo = IPO.objects.get(pk=pk)
        except IPO.DoesNotExist:
            return Response({'error': 'IPO not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IPOSerializer(ipo)
        return Response(serializer.data, status=status.HTTP_200_OK)

# IPO Statistics for Dashboard with improvements
class IPOStatistics(APIView):
    def get(self, request):
        # Fetch query params (if any)
        status_filter = request.query_params.get('status', None)
        min_return = request.query_params.get('min_return', None)

        # Start with all IPOs
        ipo_query = IPO.objects.all()

        # Filter by status if provided
        if status_filter:
            ipo_query = ipo_query.filter(status=status_filter)

        # Filter by minimum return if provided
        if min_return:
            ipo_query = ipo_query.filter(current_return__gt=min_return)

        # Calculating statistics
        total_ipo = ipo_query.count()
        ipo_in_gain = ipo_query.filter(current_return__gt=0).count()
        ipo_in_loss = ipo_query.filter(current_return__lt=0).count()

        # Count IPOs in different statuses (Upcoming, New Listed, Ongoing)
        upcoming = ipo_query.filter(status="Upcoming").count()
        new_listed = ipo_query.filter(status="New Listed").count()
        ongoing = ipo_query.filter(status="Ongoing").count()

        # Prepare the data dictionary
        data = {
            "total_ipo": total_ipo,
            "ipo_in_gain": ipo_in_gain,
            "ipo_in_loss": ipo_in_loss,
            "upcoming": upcoming,
            "new_listed": new_listed,
            "ongoing": ongoing,
        }

        # Return the response with data
        return Response(data, status=status.HTTP_200_OK)

