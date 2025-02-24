from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import ReservationSerializer,ReservationHistorySerializer,ReservationGetSerializer


class ReservationLC(ListCreateAPIView):
    queryset = ReservationSerializer.Meta.model.objects.all()
    serializer_class = ReservationSerializer


class ReservationRUD(RetrieveUpdateDestroyAPIView):
    queryset = ReservationGetSerializer.Meta.model.objects.all()
    serializer_class = ReservationGetSerializer


class ReservationHist(ListAPIView):
    queryset = ReservationHistorySerializer.Meta.model.objects.all()
    serializer_class = ReservationHistorySerializer
