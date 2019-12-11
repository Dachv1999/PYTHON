from django.urls import path
from .views import ComponenteListView, ComponenteUpdateView, ComponenteDeleteView, ComponenteCreateView

app_name = "componente"
urlpatterns = [
    path('', ComponenteListView.as_view(), name='componente-list'),
    path('crear/', ComponenteCreateView.as_view(), name='componente-crear'),
    path('actualizar/<int:pk>', ComponenteUpdateView.as_view(), name='componente-actualizar'),
    path('eliminar/<int:pk>', ComponenteDeleteView.as_view(), name='componente-eliminar'),
]