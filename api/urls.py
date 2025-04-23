

from django.urls import path
from api.views import SignUpView,ExpenseCreateListView

urlpatterns=[

    path("register/",SignUpView.as_view()),

    path("expenses/",ExpenseCreateListView.as_view())
]