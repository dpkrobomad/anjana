from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
  
    first_name=models.CharField(max_length=50,default="")
    last_name=models.CharField(max_length=50,default="")
    category = models.CharField(max_length=50,default="Customer")
    email=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    city=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    country=models.CharField(max_length=50,default="")
    zipcode =models.CharField(max_length=8,default="")
    registered_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name 


class ServiceCats(models.Model):    
    name=models.CharField(max_length=50,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return  self.name

class ServiceName(models.Model):    
    name=models.ForeignKey(ServiceCats,on_delete=models.CASCADE)
    rate=models.CharField(max_length=50,default="")
    technician_name=models.ForeignKey(Account,on_delete=models.CASCADE)
    details=models.CharField(max_length=50,default="") 
    image=models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return  str(self.name)

class Booking(models.Model): 
    CHOICES =[
    ('Processing', 'Processing'),
    ('Approved', 'Approved'),
    ('Send Techinician', 'Send Techinician'),
    ('Done', 'Done'),
    ('Rejected', 'Rejected'),
] 
    service_id=models.ForeignKey(ServiceName,on_delete=models.CASCADE)
    technician_name=models.ForeignKey(Account,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    date=models.DateField(max_length=50,default="")
    description=models.TextField(default="")    
    status=models.CharField(max_length=50,default="",choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return  self.customer_id.name

class Feedback(models.Model):
    booking_id=models.ForeignKey(Booking,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Account,on_delete=models.CASCADE)    
    comment=models.TextField(default="") 
    
    def __str__(self):
          return  self.post_id

