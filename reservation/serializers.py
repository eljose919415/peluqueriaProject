from rest_framework import serializers
from .models import Reservation, ReservationHistory
from base.serializers import CustomUserSerializer


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def to_internal_value(self, data):
        user = self.context["request"].user
        data["user"] = user.id
        return super().to_internal_value(data)

    def to_representation(self, instance):
        reservation_date = instance.reservation_date_first
        return {
            "id": instance.id,
            "phone": instance.phone,
            "reservationDay": (
                reservation_date.strftime("%d/%m/%Y %H:%M") if reservation_date else ""
            ),
            "user": CustomUserSerializer().to_representation(instance.user)["username"],
        }


class ReservationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def update(self, instance, validated_data):
        validated_data['reservation_date_first']=self.initial_data['reservationDay']
        previous = instance.reservation_date_first
        self.validate(validated_data)
        new = validated_data.get("reservation_date_first", previous)
        if previous != new:
            phone = validated_data["phone"]
            user = validated_data["user"]
            person = (
                f"{user.first_name}{user.last_name}"
                if user.first_name and user.last_name
                else user.username
            )
            reserva = ReservationHistory(
                phone=phone,
                email=user.email,
                person=person,
                reservation_date=new,
            )
            reserva.save()
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        reservation_date = instance.reservation_date_first
        ff=isinstance(reservation_date,str)
        if reservation_date and isinstance(reservation_date,str) != True:
            reservation_date = instance.reservation_date_first.strftime(
                "%Y-%m-%dT%H:%M"
            )
        user = CustomUserSerializer().to_representation(instance.user)
        return {
            "id": instance.id,
            "phone": instance.phone,
            "reservationDay": reservation_date,
            "user": user["username"],
            "userId": user["id"],
        }


class ReservationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationHistory
        fields = "__all__"
