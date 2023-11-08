from rest_framework.serializers import ModelSerializer
from .models import FlashCard


class CreateFlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('user','question', 'answer')
        
class UpdateFlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('question', 'answer')