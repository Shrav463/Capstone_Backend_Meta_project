from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   # Added booking_date and booking_time fields for bookings
   booking_date = models.DateField(null=True, blank=True) # Set null=True, blank=True if not strictly required
   booking_time = models.TimeField(null=True, blank=True) # Set null=True, blank=True if not strictly required
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return f"{self.first_name} {self.last_name} - {self.booking_date} {self.booking_time}"

   class Meta:
      # Optional: Add a unique constraint if desired
      unique_together = ('first_name', 'last_name', 'booking_date', 'booking_time', 'guest_number')


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   menu_item_description = models.TextField(max_length=1000, default=' ')

   def __str__(self):
        return self.name