from channels.generic import websockets
from channels.routing import route, route_class
from devicelocation.bindings import LocationBinding


class APIDemultiplexer(websockets.WebsocketDemultiplexer):
    # mapping = {
    #     "locations": "location_channel",
    # }
    consumers = {
        'locations': LocationBinding.consumer,
    }


channel_routing = [
    route_class(APIDemultiplexer),
    # route('location_channel', LocationBinding.consumer)
]