from django.shortcuts import render

# Create your views here.


from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView

from api.serializers import UserSerializer,ExpenseSerializer

from rest_framework import authentication,permissions

from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Expense

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class ExpenseCreateListView(CreateAPIView,ListAPIView):

    serializer_class=ExpenseSerializer

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        
        return Expense.objects.filter(owner=self.request.user)
    


class ExpenseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    serializer_class=ExpenseSerializer

    queryset=Expense.objects.all()

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]






