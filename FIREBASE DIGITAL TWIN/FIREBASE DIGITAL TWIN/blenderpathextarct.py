import bpy
import csv

# Get the selected object
obj = bpy.context.active_object

# Get all vertex coordinates
coords = [v.co for v in obj.data.vertices]

# Sort points by distance from origin to maintain order
coords.sort(key=lambda x: x.length)

# Write to CSV
csv_path = "C://Users//tsaya//Downloads//file.csv"  # Change this!
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['X', 'Y', 'Z'])  # Header
    
    # Write start point (first vertex)
    writer.writerow([coords[0].x, coords[0].y, coords[0].z])
    
    # Write all intermediate points
    for coord in coords[1:-1]:
        writer.writerow([coord.x, coord.y, coord.z])
    
    # Write end point (last vertex)
    writer.writerow([coords[-1].x, coords[-1].y, coords[-1].z])

print(f"Path exported to {csv_path}")