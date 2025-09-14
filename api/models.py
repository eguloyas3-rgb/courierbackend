from django.db import models


class Track(models.Model):
    tracking_id = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.tracking_id
    
    
    
class TrackingPackage(models.Model):
       track = models.ForeignKey(Track, on_delete=models.CASCADE)
       latest_update = models.CharField(max_length=255, blank=True, null=True)
       Update_text = models.TextField(blank=True, null=True)
       delivered_or_complain = models.TextField(blank=True, null=True)
       Arrived_location = models.CharField(blank=True, null=True)
       Arrived_location_date = models.CharField(blank=True, null=True)
       Add_date_to_next_facility = models.CharField(blank=True, null=True)
       package_arrived_at_Shiparama_Facility = models.TextField(blank=True, null=True)
       package_arrived_at_Shiparama_Facility_date = models.CharField(blank=True, null=True)
       created = models.DateField(auto_now_add=True)
       
       def __str__(self):
            return f'{self.track} - {self.latest_update}'



class Label(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()   

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
    
  

class Complaint(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.track.tracking_id}"

       
       
        
        
        
        



class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

        
