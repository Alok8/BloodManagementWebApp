from django.db import models

class Donor(models.Model):
    donor_name = models.CharField(max_length=200)
    donor_age=models.IntegerField()
    donor_blood_group=models.CharField(max_length=10)
    donor_email = models.EmailField()
    donor_contact = models.CharField(max_length=20)
    donor_address=models.CharField(max_length=200)
    donor_donated_blood_amt=models.IntegerField()
    donation_date=models.DateField()
    donor_received_blood_amt=models.IntegerField()
    donor_received_blood_group=models.CharField(max_length=10)
    receiving_date=models.DateField()


    def __str__(self):
        return self.donor_name