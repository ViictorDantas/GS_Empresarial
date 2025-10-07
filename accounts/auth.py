from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password

from accounts.models import User
from companies.models import Enterprise, Employee


class Autentication:
    """
    Classe responsável pela autenticação de usuários no sistema.
    Esta classe fornece métodos para registrar novos usuários e autenticar usuários existentes.
    
    Methods:
        signup: Registra um novo usuário no sistema.
        signin: Autentica um usuário existente no sistema.
    """
    def signin(self, email=None, password=None) -> User:
        exception_auth = AuthenticationFailed("Email e/ou senha incorretos")
        user_exists = User.objects.filter(email=email).exists()

        if not user_exists:
            raise exception_auth
        
        user = User.objects.filter(email=email).first()

        if not check_password(password, user.password):
            raise exception_auth
        
        return user
    
    def signup(self, name, email, password, type_account='owner', company_id=False) -> User:
        if name == '' or email == '' or password == '':
            raise APIException("Nome, email e senha são obrigatórios")
        
        if type_account == 'employee' and not company_id:
            raise APIException("ID da empresa é obrigatório para cadastro de funcionário")

        user = User

        if user.objects.filter(email=email).exists():
            raise APIException("Email já cadastrado")
        
        password_hashed = make_password(password)

        created_user = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=True if type_account == 'owner' else False
        )

        if type_account == 'owner':
            created_enterprise = Enterprise.objects.create(
                name="Nome da Empresa",
                user_id=created_user.id
            )

        if type_account == 'employee':
            Employee.objects.create(
                entreprise_id=company_id or created_enterprise.id,
                user_id=created_user.id
            )
        return created_user