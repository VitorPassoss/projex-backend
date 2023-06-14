from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DashboardInfoSerializer
from rest_framework.permissions import IsAuthenticated


class DashboardInfo(APIView):
    permission_classes = [ IsAuthenticated ]
    def get(self, request):
        serializer = DashboardInfoSerializer(instance={"obj": "obj"}, context={"request": request})
        return Response(serializer.data)





