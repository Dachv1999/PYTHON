from django.urls import path
from .views import AmbienteListView, AmbienteUpdateView, AmbienteDeleteView, AmbienteCreateView

app_name = "ambiente"
urlpatterns = [
    path('', AmbienteListView.as_view(), name='ambiente-list'),
    path('crear/', AmbienteCreateView.as_view(), name='ambiente-crear'),
    path('actualizar/<int:pk>', AmbienteUpdateView.as_view(), name='ambiente-actualizar'),
    path('eliminar/<int:pk>', AmbienteDeleteView.as_view(), name='ambiente-eliminar'),
]
