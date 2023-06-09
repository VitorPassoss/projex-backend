from rest_framework.views import APIView
from rest_framework.response import Response
from apps.properties.models.property import Property
from apps.properties.serializers import PropertySerializer
from rest_framework import status


class CreateProperties(APIView):
    serializer_class = PropertySerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Property registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetMyProperties(APIView):
    def get(self, request):
        try:
            props_stock = Property.objects.filter(user_fk=request.user.pk, availability= True)
            props_serialized = PropertySerializer(props_stock, many=True).data
            response_data = {
                'properties': props_serialized
            }
            return Response(response_data)
        except Property.DoesNotExist:
            return Response({"message": "Error in query properties for user"})
        

class GetMyHistory(APIView):
    def get(self, request):
        try:
            props_stock = Property.objects.filter(user_fk=request.user.pk, availability= False)
            props_serialized = PropertySerializer(props_stock, many=True).data
            response_data = {
                'properties': props_serialized
            }
            return Response(response_data)
        except Property.DoesNotExist:
            return Response({"message": "Error in query properties for user"})
        




