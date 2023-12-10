from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import CreateFlashCardSerializer, UpdateFlashCardSerializer
from rest_framework.response import Response
from .models import FlashCard
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status


class CreateFlashCardView(APIView):
    def post(self, request):

        flash_card = CreateFlashCardSerializer(data=request.data)
        flash_card.is_valid(raise_exception=True)
        flash_card.validated_data
        flash_card.save()
        
        return Response(flash_card.data, status=status.HTTP_201_CREATED)


class UpdateFlashCardView(APIView):

    def get(self, request, id):

        old_data = get_object_or_404(FlashCard, id=id)
        serializer = CreateFlashCardSerializer(old_data)
        return Response(serializer.data)
    
    def put(self, request, id):
        
        old_data = get_object_or_404(FlashCard, id=id)
        
        new_data = UpdateFlashCardSerializer(data=request.data, instance=old_data)
        
        new_data.is_valid(raise_exception=True)
        
        new_data.save()
        
        return Response(new_data.data, status=status.HTTP_200_OK)
        
        
class DeleteFlashCardView(APIView):
    
    def delete(self, request, id):
        
        selected_card = get_object_or_404(FlashCard, id=id)
        selected_card.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListFlashCardsView(APIView):
    
    def get(self, request, user_id):
        
        all_user_cards = get_list_or_404(FlashCard, user__id=user_id)
        
        serializer = CreateFlashCardSerializer(all_user_cards, many=True)
        
        return Response(serializer.data)
    
    