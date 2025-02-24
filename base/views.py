from .serializers import RefreshTokenSerializer, CustomUserSerializer, ImageManageSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView


# Create your views here.
class LogoutView(APIView):
    serializer_class = RefreshTokenSerializer

    # permission_classes=(permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        sz = self.serializer_class(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response({"msg": "Vuelva pronto"}, status=status.HTTP_200_OK)


# region CustomUser
class Register(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUserSerializer.Meta.model.objects.all()


class CustomUserL(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUserSerializer.Meta.model.objects.all()


class CustomUserRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUserSerializer.Meta.model.objects.all()


# endregion
# region ImagesManage
class ImagesManageLC(ListCreateAPIView):
    serializer_class = ImageManageSerializer
    queryset = ImageManageSerializer.Meta.model.objects.all()


class ImagesMangeRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = ImageManageSerializer
    queryset = ImageManageSerializer.Meta.model.objects.all()

# endregion
