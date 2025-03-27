from django.db import models

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ("gas_leak", "Gas Leak"),
        ("low_pressure", "Low Pressure"),
        ("meter_issue", "Meter Issue"),
        ("billing", "Billing Issue"),
        ("other", "Other"),
    ]

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to="attachments/", blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service_type} - {self.status}"
