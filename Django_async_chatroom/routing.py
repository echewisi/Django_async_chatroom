from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, UrlRouter
import chatroom.routing

application= ProtocolTypeRouter({    'websocket': AuthMiddlewareStack(
        UrlRouter(
            chatroom.routing.websocket_urlpatterns
        ),
    )}

)