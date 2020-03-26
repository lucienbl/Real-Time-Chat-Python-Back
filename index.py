from flask import Flask
from flask_socketio import SocketIO
from src.ChatSocketHandler import ChatSocketHandler

# Initialization
app = Flask(__name__)
socketio = SocketIO(app)


# HTTP routes
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"


# Register namespaces
socketio.on_namespace(ChatSocketHandler('/chat'))

# Run the app
if __name__ == '__main__':
    socketio.run(app)
