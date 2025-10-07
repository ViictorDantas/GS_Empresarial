from django.db import models



class Enterprise(models.Model):
    """Modelo que representa uma empresa no sistema.
    Attributes:
        name (str): Nome da empresa (máximo 255 caracteres)
        user (User): Usuário proprietário da empresa

    Example:
        >>> enterprise = Enterprise.objects.create(
        ...     name="Minha Empresa",
        ...     user=user_instance
        ... )
        >>> print(enterprise.name)
        'Minha Empresa'
    """
    name = models.CharField(max_length=255)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='enterprises')

    def __str__(self):
        return self.name