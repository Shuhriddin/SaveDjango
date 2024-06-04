from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=100,verbose_name="Client name",help_text="Enter client name",null=True,blank=True)
    username = models.CharField(max_length=100,verbose_name="Client username",help_text="Enter client username",null=True,blank=True)
    telegram_id = models.CharField(max_length=30,verbose_name="Telegram ID",help_text="Enter telegram ID",unique=True)
    language = models.CharField(max_length=10,default="uz",verbose_name="Client System Language",help_text="Enter client system language", null=True, blank=True)
    # phone = models.CharField(max_length=100,verbose_name="Client Phone Number",help_text="Enter client phone",null=True,blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name