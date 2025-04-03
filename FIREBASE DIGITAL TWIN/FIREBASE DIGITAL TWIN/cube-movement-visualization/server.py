#3D Visualization Project with Cube(Server Side)
'''
from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*", logger=True, engineio_logger=True)

# Store the latest position
latest_position = {'x': 0, 'y': 0, 'z': 0}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/')
def handle_connect():
    print('Client connected')
    socketio.emit('position_update', latest_position, namespace='/')

@socketio.on('update_position', namespace='/')
def handle_position_update(data):
    global latest_position
    latest_position = data
    socketio.emit('position_update', data, namespace='/', broadcast=True)

if __name__ == '__main__':
    print("Server running at: http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)'''


#3D Visualization Project with Cube and Cone(Server Side)
from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*", logger=True, engineio_logger=True)

# Store latest positions
latest_positions = {
    'cube': {'x': 0, 'y': 0, 'z': 0},
    'cone': {'x': 2, 'y': 0, 'z': 0}  # Initial cone position
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/')
def handle_connect():
    print('Client connected')
    # Send initial positions for both shapes
    socketio.emit('position_update', {
        'shape': 'cube',
        'x': latest_positions['cube']['x'],
        'y': latest_positions['cube']['y'],
        'z': latest_positions['cube']['z']
    }, namespace='/')
    
    socketio.emit('position_update', {
        'shape': 'cone',
        'x': latest_positions['cone']['x'],
        'y': latest_positions['cone']['y'],
        'z': latest_positions['cone']['z']
    }, namespace='/')

@socketio.on('update_position', namespace='/')
def handle_position_update(data):
    global latest_positions
    shape = data['shape']
    latest_positions[shape] = {
        'x': data['x'],
        'y': data['y'],
        'z': data['z']
    }
    socketio.emit('position_update', data, namespace='/', broadcast=True)

if __name__ == '__main__':
    print("Server running at: http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)