from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Camera calibration values (from Part 1)
fx, fy = 1667.56, 1983.22   # focal lengths
cx, cy = 1073.54, 703.15    # principal point coordinates
Z = 34.0                    # distance from camera to object (cm)

@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calculate real-world distances between two image points (p1, p2).
    Uses pinhole camera model equations.
    """
    data = request.get_json()
    p1, p2 = data['p1'], data['p2']

    # Extract pixel coordinates
    x1, y1 = p1['x'], p1['y']
    x2, y2 = p2['x'], p2['y']

    # Convert pixel coordinates to real-world coordinates
    X1, Y1 = (x1 - cx) * Z / fx, (y1 - cy) * Z / fy
    X2, Y2 = (x2 - cx) * Z / fx, (y2 - cy) * Z / fy

    # Compute Euclidean distance in cm
    distance = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)

    return jsonify({'distance_cm': distance})

if __name__ == "__main__":
    app.run(debug=True)
