from flask import request
from flask_socketio import SocketIO

from heartbeat import counts

socketio = SocketIO()  # pylint: disable=invalid-name

@socketio.on('connect', namespace='/heartbeat')
def connect(data):
    page = data['page']
    counts.incriment(page)


@socketio.on('disconnect', namespace='/hearbeat')
def disconnect(data):
    page = data['page']
    counts.decrement(page)
