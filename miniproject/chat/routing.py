from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path("ws/socket-server/<str:user>/<str:room>",consumers.chatconsumer.as_asgi())
]