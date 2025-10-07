from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission
from django.conf import settings

class User(AbstractBaseUser):
    """
    Modelo que representa um usuário no sistema.
    Este modelo é responsável por armazenar informações sobre os usuários,
    incluindo suas credenciais de login e permissões.

    Attributes:
        name (str): Nome completo do usuário (máximo 255 caracteres)
        email (str): Endereço de e-mail único do usuário
        is_owner (bool): Indica se o usuário é o proprietário da empresa

    Example:
        >>> user = User.objects.create(
        ...     name="João da Silva",
        ...     email="joao@example.com",
        ...     is_owner=True
        ... )
        >>> print(user.name)
        'João da Silva'
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class Group(models.Model):
    """
    Modelo que representa um grupo de usuários.
    Este modelo é responsável por armazenar informações sobre grupos,
    incluindo seu nome e a empresa à qual pertencem.

    Attributes:
        name (str): Nome do grupo (máximo 255 caracteres)
        enterprise (Enterprise): Empresa à qual o grupo pertence

    Example:
        >>> group = Group.objects.create(
        ...     name="Desenvolvedores",
        ...     enterprise=enterprise_instance
        ... )
        >>> print(group.name)
        'Desenvolvedores'
    """
    name = models.CharField(max_length=255)
    enterprise = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class GroupPermission(models.Model):
    """
    Modelo que representa a associação entre grupos e permissões.
    """
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class UserGroup(models.Model):
    """
    Modelo que representa a associação entre usuários e grupos.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)