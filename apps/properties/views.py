from rest_framework.views import APIView
from rest_framework.response import Response
from apps.properties.models.property import Property
from apps.properties.serializers import PropertySerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class CreateProperties(APIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = PropertySerializer
    def post(self, request):
        data = request.data.copy()
        data['user_fk'] = request.user.pk

        if data.get('price_seller') is None:
            del data['price_seller']

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Property registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

class GetMyProperties(APIView):
    permission_classes = [ IsAuthenticated ]
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
        
    def post(self, request):
        pk_props = request.data.get('pk')
        price_seller = request.data.get('price_seller')
        print(price_seller)
        try:
            get_props = Property.objects.get(pk=pk_props)
            get_props.price_seller = price_seller
            get_props.availability = False
            get_props.save()
            return Response({"message": "Property update successfully"}, status=status.HTTP_201_CREATED)
        except Property.DoesNotExist:
            return Response({"message": "Error in query properties for user"})



        

class GetMyHistory(APIView):
    permission_classes = [ IsAuthenticated ]
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
        




