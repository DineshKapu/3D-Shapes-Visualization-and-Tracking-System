import open3d as o3d
import numpy as np
import threading
import time
import keyboard  # pip install keyboard

class SharedCube:
    def __init__(self):
        self.mesh = o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0)
        self.mesh.compute_vertex_normals()
        self.mesh.paint_uniform_color([0.5, 0.5, 0.8])  # Light blue
        self.position = np.array([0.0, 0.0, 0.0])
        self.move_step = 0.1
        self.lock = threading.Lock()

    def move(self, direction):
        with self.lock:
            if direction == 'left':
                self.position[0] -= self.move_step
                self.mesh.translate(np.array([-self.move_step, 0, 0]))
            elif direction == 'right':
                self.position[0] += self.move_step
                self.mesh.translate(np.array([self.move_step, 0, 0]))
            elif direction == 'up':
                self.position[1] += self.move_step
                self.mesh.translate(np.array([0, self.move_step, 0]))
            elif direction == 'down':
                self.position[1] -= self.move_step
                self.mesh.translate(np.array([0, -self.move_step, 0]))
            elif direction == 'forward':
                self.position[2] += self.move_step
                self.mesh.translate(np.array([0, 0, self.move_step]))
            elif direction == 'backward':
                self.position[2] -= self.move_step
                self.mesh.translate(np.array([0, 0, -self.move_step]))

def control_window(cube):
    vis = o3d.visualization.VisualizerWithKeyCallback()
    vis.create_window(window_name="Control Window (Use WASD-QE to move)")
    vis.add_geometry(cube.mesh)
    
    # Register key callbacks
    def move_left(vis):
        cube.move('left')
        vis.update_geometry(cube.mesh)
    
    def move_right(vis):
        cube.move('right')
        vis.update_geometry(cube.mesh)
    
    def move_up(vis):
        cube.move('up')
        vis.update_geometry(cube.mesh)
    
    def move_down(vis):
        cube.move('down')
        vis.update_geometry(cube.mesh)
    
    def move_forward(vis):
        cube.move('forward')
        vis.update_geometry(cube.mesh)
    
    def move_backward(vis):
        cube.move('backward')
        vis.update_geometry(cube.mesh)
    
    vis.register_key_callback(ord('A'), move_left)
    vis.register_key_callback(ord('D'), move_right)
    vis.register_key_callback(ord('W'), move_up)
    vis.register_key_callback(ord('S'), move_down)
    vis.register_key_callback(ord('Q'), move_forward)
    vis.register_key_callback(ord('E'), move_backward)
    
    while True:
        if not vis.poll_events():
            break
        vis.update_renderer()
    vis.destroy_window()

def viewer_window(cube):
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="Viewer Window (Watching cube movement)")
    vis.add_geometry(cube.mesh)
    
    while True:
        with cube.lock:
            vis.update_geometry(cube.mesh)
        
        if not vis.poll_events():
            break
        vis.update_renderer()
        time.sleep(0.01)  # Small delay to reduce CPU usage
    vis.destroy_window()

# Create shared cube object
cube = SharedCube()

# Create and run windows in separate threads
control_thread = threading.Thread(target=control_window, args=(cube,))
viewer_thread = threading.Thread(target=viewer_window, args=(cube,))

control_thread.start()
viewer_thread.start()

control_thread.join()
viewer_thread.join()