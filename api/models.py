from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone=models.CharField(max_length=15,unique=True)


class Expense(models.Model):
    EXPENSE_CATEGORIES = (
        ('housing', 'Housing'),
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('health', 'Health'),
        ('education', 'Education'),
        ('personal', 'Personal'),
        ('entertainment', 'Entertainment'),
        ('bills', 'Bills'),
        ('shopping', 'Shopping'),
        ('miscellaneous', 'Miscellaneous'),
    )
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100,choices=EXPENSE_CATEGORIES,default="personal")
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"


