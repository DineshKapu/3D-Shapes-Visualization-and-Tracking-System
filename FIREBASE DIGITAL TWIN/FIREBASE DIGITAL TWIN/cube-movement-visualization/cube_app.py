#3D Visualization Project with Cube
'''
import open3d as o3d
from cube_controller import CubeController
from flask_socketio import SocketIO
import socketio
import time

class VisualizerApp:
    def __init__(self):
        self.cube = CubeController()
        self.vis = None
        self.sio = socketio.Client()
        
        # Connect to the server
        self.sio.connect('http://localhost:5000')
        
    def initialize_visualizer(self):
        self.vis = o3d.visualization.VisualizerWithKeyCallback()
        try:
            self.vis.create_window(
                window_name="Cube Controller (WASD-QE to move)",
                width=1024,
                height=768
            )
            self.vis.add_geometry(self.cube.mesh)
            
            # Set initial view
            ctr = self.vis.get_view_control()
            ctr.set_front([0, 0, -1])
            ctr.set_lookat([0, 0, 0])
            ctr.set_up([0, 1, 0])
            ctr.set_zoom(0.8)
            return True
        except Exception as e:
            print(f"Failed to initialize visualizer: {e}")
            return False

    def run(self):
        if not self.initialize_visualizer():
            return

        key_mapping = {
            ord('A'): 'left',
            ord('D'): 'right',
            ord('W'): 'up',
            ord('S'): 'down',
            ord('Q'): 'forward',
            ord('E'): 'backward'
        }

        for key, direction in key_mapping.items():
            self.vis.register_key_callback(key, self.create_move_callback(direction))

        print("Use WASD-QE keys to move the cube")
        print("Web interface available at http://localhost:5000")

        try:
            while True:
                if not self.vis.poll_events():
                    break
                self.vis.update_renderer()
                time.sleep(0.01)
        finally:
            self.vis.destroy_window()
            self.sio.disconnect()

    def create_move_callback(self, direction):
        def callback(vis):
            self.cube.move(direction)
            vis.update_geometry(self.cube.mesh)
            # Emit position update through socketio
            self.sio.emit('update_position', {
                'x': float(self.cube.position[0]),
                'y': float(self.cube.position[1]), 
                'z': float(self.cube.position[2])
            })
        return callback

if __name__ == "__main__":
    # Start visualizer
    visualizer = VisualizerApp()
    visualizer.run()'''

#3D Visualization Project with Cube and Cone
import open3d as o3d
from shapes_controller import ShapesController
import socketio
import time

class VisualizerApp:
    def __init__(self):
        self.shapes = ShapesController()
        self.vis = None
        self.sio = socketio.Client()
        
        # Connect to the server
        self.sio.connect('http://localhost:5000')
        
    def initialize_visualizer(self):
        self.vis = o3d.visualization.VisualizerWithKeyCallback()
        try:
            self.vis.create_window(
                window_name="3D Shapes Controller",
                width=1024,
                height=768
            )
            # Add both shapes to visualizer
            self.vis.add_geometry(self.shapes.cube['mesh'])
            self.vis.add_geometry(self.shapes.cone['mesh'])
            
            # Set initial view
            ctr = self.vis.get_view_control()
            ctr.set_front([0, 0, -1])
            ctr.set_lookat([0, 0, 0])
            ctr.set_up([0, 1, 0])
            ctr.set_zoom(0.8)
            return True
        except Exception as e:
            print(f"Failed to initialize visualizer: {e}")
            return False

    def run(self):
        if not self.initialize_visualizer():
            return

        # Cube controls (WASD-QE)
        cube_controls = {
            ord('A'): 'left',
            ord('D'): 'right',
            ord('W'): 'up',
            ord('S'): 'down',
            ord('Q'): 'forward',
            ord('E'): 'backward'
        }

        # Cone controls (Arrow keys + TAB/SHIFT)
        cone_controls = {
            262: 'right',    # Right arrow
            263: 'left',     # Left arrow
            265: 'up',       # Up arrow
            264: 'down',     # Down arrow
            9: 'forward',    # TAB
            304: 'backward'  # Left Shift
        }

        # Register cube callbacks
        for key, direction in cube_controls.items():
            self.vis.register_key_callback(key, self.create_move_callback('cube', direction))

        # Register cone callbacks
        for key, direction in cone_controls.items():
            self.vis.register_key_callback(key, self.create_move_callback('cone', direction))

        print("Controls:")
        print("Cube: WASD-QE")
        print("Cone: Arrow Keys + TAB/SHIFT")
        print("Web interface available at http://localhost:5000")

        try:
            while True:
                if not self.vis.poll_events():
                    break
                self.vis.update_renderer()
                time.sleep(0.01)
        finally:
            self.vis.destroy_window()
            self.sio.disconnect()

    def create_move_callback(self, shape, direction):
        def callback(vis):
            pos = self.shapes.move_shape(shape, direction)
            vis.update_geometry(self.shapes.cube['mesh'])
            vis.update_geometry(self.shapes.cone['mesh'])
            # Emit position update through socketio
            self.sio.emit('update_position', {
                'shape': shape,
                'x': pos['x'],
                'y': pos['y'], 
                'z': pos['z']
            })
        return callback

if __name__ == "__main__":
    visualizer = VisualizerApp()
    visualizer.run()