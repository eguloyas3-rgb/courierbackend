from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Track, TrackingPackage
from .serializers import *
from rest_framework.permissions import AllowAny
# import json
# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt



class TrackingAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, tracking_id):
        try:
            track = Track.objects.get(tracking_id=tracking_id)
        except Track.DoesNotExist:
            return Response(
                {"error": "Invalid tracking ID"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Get all related packages
        packages = TrackingPackage.objects.filter(track=track)

        track_data = TrackSerializer(track).data
        package_data = TrackingPackageSerializer(packages, many=True).data

        return Response({
            "track": track_data,
            "packages": package_data
        })


# class TrackingAllAPIView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request):
#         tracks = Track.objects.all()
#         packages = TrackingPackage.objects.all()

#         track_data = TrackSerializer(tracks, many=True).data
#         package_data = TrackingPackageSerializer(packages, many=True).data

#         return Response({
#             "tracks": track_data,
#             "packages": package_data
#         })



class PingAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "pong"})
    
    
    

# views.py


class ContactAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # triggers signal to send email
            return Response({"message": "Message sent successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# cloudflare tunnel

# @csrf_exempt
# def verify_turnstile(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         token = data.get("token")
#         secret = "YOUR_SECRET_KEY"

#         resp = requests.post(
#             "https://challenges.cloudflare.com/turnstile/v0/siteverify",
#             data={"secret": secret, "response": token}
#         )
#         result = resp.json()
#         return JsonResponse({"success": result.get("success", False)})
#     return JsonResponse({"success": False, "message": "Invalid method"})
