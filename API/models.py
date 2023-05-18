from django.db import models


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=25, verbose_name="name")
    last_name = models.CharField(max_length=50, verbose_name="last name")
    phone_number = models.IntegerField(verbose_name="phone number")
    email = models.EmailField(max_length=50, verbose_name="email")

    class Meta:
        db_table = "client"

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.DateTimeField()

    APPOINTMENT_TYPE_CHOICES = (
        ('haircut', 'Haircut'),
        ('manicure', 'Manicure'),
        ('pedicure', 'Pedicure'),
        ('hairstyling', 'Hairstyling'),
        ('makeup', 'Makeup'),
    )

    appointment_type = models.CharField(max_length=50, choices=APPOINTMENT_TYPE_CHOICES)

    class Meta:
        db_table = "appointment"

    def __str__(self):
        return f'Appointment for {self.client} on {self.appointment_date}'
