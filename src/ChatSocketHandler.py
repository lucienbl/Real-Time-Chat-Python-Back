from flask_socketio import Namespace, emit, join_room
from src import SocketEvents


class ChatSocketHandler(Namespace):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    @staticmethod
    def on_join_channel(data):
        join_room(data['room_id'])
        print(data['user_id'] + ' has entered the room ' + data['room_id'])

    @staticmethod
    def on_send_message(data):
        emit(SocketEvents.message_added, data, room=data['room_id'], include_self=True)
