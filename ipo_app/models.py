from django.db import models

# Create your models here.
from django.db import models

class IPO(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField()
    price_band = models.CharField(max_length=100)
    opening_date = models.DateField()
    closing_date = models.DateField()
    issue_size = models.FloatField()
    issue_type = models.CharField(max_length=100)
    listing_date = models.DateField()
    status = models.CharField(max_length=100)
    ipo_price = models.FloatField()
    listing_price = models.FloatField()
    listing_gain = models.FloatField()
    current_market_price = models.FloatField()
    current_return = models.FloatField()
    rhp_pdf = models.FileField(upload_to='rhp_pdfs/')
    drhp_pdf = models.FileField(upload_to='drhp_pdfs/')

    def __str__(self):
        return self.name
