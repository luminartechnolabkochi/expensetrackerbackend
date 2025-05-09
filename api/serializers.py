

from rest_framework import serializers

from api.models import User,Expense

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["id","username","email","password","phone"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:

        model=Expense

        fields="__all__"

        read_only_fields=[
            "id",
            "owner",
            "date"
        ]

