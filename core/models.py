from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True) # Opcional
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True) # Se guarda la fecha automáticamente

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.email})"

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"