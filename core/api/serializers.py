from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico

class PontoTuristicoSeralizer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos')