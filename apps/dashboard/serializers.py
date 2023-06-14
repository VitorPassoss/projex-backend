from rest_framework import serializers
from apps.properties.models.property import Property
from django.db.models import Sum

class DashboardInfoSerializer(serializers.Serializer):
    properties_count = serializers.SerializerMethodField()
    general_info = serializers.SerializerMethodField()

    class Meta:
        fields = ['properties_count', 'general_info']

    def get_properties_count(self, obj):
        request = self.context.get("request")
        count_stock = Property.objects.filter(user_fk=request.user.pk, availability=True).count()
        count_seller = Property.objects.filter(user_fk=request.user.pk, availability=False).count()
        count_total = Property.objects.filter(user_fk=request.user.pk).count()
        return {
            'count_stock': count_stock,
            'count_seller': count_seller,
            'count_total': count_total,
        }

    def get_general_info(self, obj):
        request = self.context.get("request")

        total_bought = Property.objects.filter(user_fk=request.user.pk).aggregate(Sum('price_buyer'))['price_buyer__sum']
        total_sold = Property.objects.filter(user_fk=request.user.pk).aggregate(Sum('price_seller'))['price_seller__sum']

        # Inicializar como zero se for None
        total_bought = total_bought if total_bought is not None else 0
        total_sold = total_sold if total_sold is not None else 0

        # Calculate profit margin
        if total_sold != 0:  # To avoid division by zero
            profit_margin = ((total_sold - total_bought) / total_sold) * 100
        else:
            profit_margin = 0

        profit_margin = round(profit_margin, 2)


        return {
            'total_bought': total_bought,
            'total_sold': total_sold,
            'profit_margin': profit_margin
        }
