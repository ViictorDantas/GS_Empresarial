from rest_framework import serializers

from .models import User



class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo User.
    Este serializer é responsável por validar e serializar os dados do usuário.
    """
    class Meta:
        model = User
        fields = (
            'id',
            'name',
           'email'
           )
        