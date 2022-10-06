# from tkinter import CASCADE
from distutils.command.upload import upload
from django.db import models
 #Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length= 20,null=True)
    last_name = models.CharField(max_length= 20,null=True)
    address = models.CharField(max_length= 15)
    email = models.EmailField()
    phone_number = models.CharField(max_length= 15,null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length= 15,choices= GENDER_CHOICES,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    id_number = models.CharField(max_length= 15,null=True)
    nationality = models.CharField(max_length= 15,null=True)
    profile_picture = models.ImageField(upload_to= 'profile_picture/',null=True)

class Wallet(models.Model):
    User_id = models.IntegerField()
    balance = models.IntegerField()
    amount = models.IntegerField()
    time = models.DateTimeField()
    # transaction = models.ForeignKey("Transaction",on_delete= models.CASCADE, related_name= "wallet_transaction")
    status = models.CharField(max_length= 15,null=True)
    history = models.DateTimeField()
    pin = models.CharField(max_length= 15,null=True)

class Account(models.Model):
    account_name = models.CharField(max_length= 15,null=True)
    account_number = models.IntegerField()
    ACCOUNTTYPE_CHOICES = (
        ('W', 'Withdrawal'),
        ('S', 'Savings'),
        ('D', 'Deposits'),
    )
    account_type = models.CharField(max_length= 15, choices= ACCOUNTTYPE_CHOICES)
    balance = models.IntegerField()
    wallet = models.ForeignKey("Wallet",on_delete= models.CASCADE, related_name= "account_wallet")
    

class Transaction(models.Model):
    transaction_code = models.CharField(max_length= 15,null=True)
    wallet_one = models.ForeignKey("Wallet",on_delete= models.CASCADE,related_name="Transaction_wallet")
    transaction_amount = models.IntegerField()
    transaction_number = models.IntegerField()  
    TRASACTION_TYPE_CHOICES = (
        ('D','Debit'),
        ('C','Credit'),
    )
    transaction_type = models.CharField(max_length= 15, choices= TRASACTION_TYPE_CHOICES)   #
    transaction_fee = models.IntegerField()
    transaction_time = models.DateField()
    # transaction_receipt = models.ForeignKey("Receipt",on_delete= models.CASCADE,related_name="transaction_transaction_receipt")  
    origin_account = models.ForeignKey("Account",on_delete= models.CASCADE,related_name="transaction_origin")
    destination_account = models.ForeignKey("Account",on_delete= models.CASCADE, related_name= "transaction_destination")

class Card(models.Model):
    card_name = models.CharField(max_length= 15,null=True)
    card_number = models.IntegerField()
    CARD_TYPE_CHOICES = (
        ('C','Credit card'),
        ('D','Debit card'),
    )
    card_type = models.CharField(max_length= 15, choices= CARD_TYPE_CHOICES)
    cvv_code = models.IntegerField()
    CARD_ISSUER_CHOICES = (
        ('V','Visa'),
        ('M','Master card'),
    )
    card_issuer = models.CharField(max_length= 15, choices= CARD_ISSUER_CHOICES)
    date_issued = models.DateTimeField()
    expiry_date = models.DateTimeField()
    wallet = models.ForeignKey("Wallet",on_delete= models.CASCADE,related_name= "card_wallet")
    account = models.ForeignKey("Account",on_delete= models.CASCADE, related_name= "card_account")
    card_status = models.CharField(max_length= 15,null=True)

class ThirdParty(models.Model):
    party_name = models.CharField(max_length= 15,null=True)
    account = models.ForeignKey("Account",on_delete= models.CASCADE, related_name= "ThirdParty_account")
    party_id = models.PositiveSmallIntegerField()
    phone_number = models.IntegerField()

class Notifications(models.Model):
    customer_name = models.CharField(max_length= 15,null=True)
    notification_date_time = models.DateTimeField()
    recipient = models.ForeignKey("Receipt",on_delete= models.CASCADE, related_name= "notification_recipient")
    STATUS = (
        ('R','Read'),
        ('U','Unread')
    )
    notification_status = models.CharField(max_length= 1, choices= STATUS)

class Receipt(models.Model):
    receipt_type = models.CharField(max_length= 8,null=True)
    receipt_date = models.DateTimeField()
    receipt_file = models.FileField()
    total_amount = models.IntegerField()
    account_number = models.IntegerField()
    transaction = models.ForeignKey("Transaction",on_delete= models.CASCADE, related_name= "receipt_transaction")

class Loan(models.Model):
    loan_number = models.IntegerField()
    loan_type = models.CharField(max_length= 15,null=True)
    loan_amount = models.IntegerField()
    loan_date = models.DateTimeField()
    wallet = models.ForeignKey("Wallet",on_delete= models.CASCADE, related_name= "loan_wallet")
    interest_rate = models.IntegerField()
    loan_guaranter = models.ForeignKey("Customer", on_delete= models.CASCADE, related_name= "loan_loan")
    loan_due_date = models.DateTimeField()
    loan_balance = models.IntegerField()
    loan_term = models.IntegerField()

class Reward(models.Model):
    transaction = models.ForeignKey("Transaction",on_delete= models.CASCADE, related_name= "reward_transaction")
    reward_date = models.DateTimeField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length= 15,choices= GENDER_CHOICES)
    reward_points = models.IntegerField()
