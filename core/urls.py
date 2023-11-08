from django.contrib import admin
from django.urls import path, include
from card.views import CreateFlashCardView, UpdateFlashCardView, ListFlashCardsView, DeleteFlashCardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('card/create/', CreateFlashCardView.as_view(), name='create-card'),
    path('card/update/<id>/', UpdateFlashCardView.as_view(), name='update-card'),
    path('card/delete/<id>/', DeleteFlashCardView.as_view(), name='delete-card'),
    path('card/list/<user_id>/', ListFlashCardsView.as_view(), name='list-card'),
]
