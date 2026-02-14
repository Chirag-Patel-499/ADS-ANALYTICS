from django.db import models

class FacebookAdStat(models.Model):
    date = models.DateField()
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    spend = models.FloatField(default=0)

    def __str__(self):
        return str(self.date)


class WhatsAppLead(models.Model):
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
