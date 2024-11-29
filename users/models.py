from django.db import models

class Akun(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # Password terenkripsi
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Customer(models.Model):
    id_akun = models.OneToOneField(Akun, on_delete=models.CASCADE)
    nama_customer = models.CharField(max_length=100)
    telepon_customer = models.CharField(max_length=15)
    alamat_customer = models.TextField()

    def __str__(self):
        return self.nama_customer


class Admin(models.Model):
    id_akun = models.OneToOneField(Akun, on_delete=models.CASCADE)
    nama_admin = models.CharField(max_length=100)
    telepon_admin = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_admin
