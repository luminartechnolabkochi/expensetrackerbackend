

from django.urls import path
from api.views import SignUpView,ExpenseCreateListView,ExpenseRetrieveUpdateDeleteView


from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[

    path("token/",TokenObtainPairView.as_view()),

    path("token/refresh/",TokenRefreshView.as_view()),

    path("register/",SignUpView.as_view()),

    path("expenses/",ExpenseCreateListView.as_view()),

    path("expenses/<int:pk>/",ExpenseRetrieveUpdateDeleteView.as_view()),
    
]