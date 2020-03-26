from flask_socketio import Namespace, emit, join_room


class ChatSocketHandler(Namespace):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    @staticmethod
    def on_join(data):
        join_room(data['room_id'])
        print(data['user_id'] + ' has entered the room ' + data['room_id'])

    @staticmethod
    def on_message_add(data):
        emit('message_add', data, room=data['room_id'], include_self=True)
