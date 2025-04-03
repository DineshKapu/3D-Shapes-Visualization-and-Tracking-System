
import numpy as np
import open3d as o3d

class CubeController:
    def __init__(self):
        self.mesh = o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0)
        self.mesh.compute_vertex_normals()
        self.mesh.paint_uniform_color([0.5, 0.5, 0.8])
        self.position = np.array([0.0, 0.0, 0.0])
        self.move_step = 0.5

    def move(self, direction):
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
