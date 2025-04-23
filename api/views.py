from django.shortcuts import render

# Create your views here.


from rest_framework.generics import CreateAPIView,ListAPIView

from api.serializers import UserSerializer,ExpenseSerializer

from rest_framework import authentication,permissions

from api.models import Expense

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class ExpenseCreateListView(CreateAPIView,ListAPIView):

    serializer_class=ExpenseSerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        
        return Expense.objects.filter(owner=self.request.user)
    







