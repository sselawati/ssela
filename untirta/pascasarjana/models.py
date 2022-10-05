from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=9)
    Nama = models.CharField(max_length=9)
    Tanggal_Lahir = models.CharField(max_length=9)
    Photo = models.CharField(max_length=9)
    Email = models.CharField(max_length=9)
    Fakultas = models.CharField(max_length=9)
    Prodi = models.CharField(max_length=9)
    Alamat_Rumah = models.CharField(max_length=9)

    def __str__(self):
        return self.NIP

class Staf(models.Model):
    NIP = models.CharField(max_length=9)
    Nama = models.CharField(max_length=9)
    Tanggal_Lahir = models.CharField(max_length=9)
    Photo = models.CharField(max_length=9)
    Email = models.CharField(max_length=9)
    Unit = models.CharField(max_length=9)
    Alamat_Rumah = models.CharField(max_length=9)

    def __str__(self):
        return self.NIP

class Mahasiswa(models.Model):
    NIP = models.CharField(max_length=9)
    Nama = models.CharField(max_length=9)
    Tanggal_Lahir = models.CharField(max_length=9)
    Photo = models.CharField(max_length=9)
    Email = models.CharField(max_length=9)
    Fakultas = models.CharField(max_length=9)
    Prodi = models.CharField(max_length=9)
    Alamat_Rumah = models.CharField(max_length=9)

    def __str__(self):
        return self.NIP

class untirta(models.Model):
    Dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    Staf = models.ForeignKey(Staf, on_delete=models.CASCADE)
    Mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)

    def __str__(self):
        return self.Dosen