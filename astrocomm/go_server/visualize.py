import plotly.graph_objects as go
import requests

# Function to simulate multiple telemetry data points
def generate_multiple_telemetry_points(n):
    points = []
    for _ in range(n):
        # Fetch telemetry data from Go server
        response = requests.get('http://localhost:8080/telemetry')
        telemetry_data = response.json()

        # Extract telemetry data
        battery_level = telemetry_data['normal']['battery_level']
        radiation_level = telemetry_data['normal']['radiation_level']
        signal_strength = telemetry_data['normal']['signal_strength']
        points.append((battery_level, radiation_level, signal_strength))
    return points

# Generate a sequence of telemetry points
telemetry_points = generate_multiple_telemetry_points(50)

# Split data into x, y coordinates for 2D plots
battery_levels = [point[0] for point in telemetry_points]
radiation_levels = [point[1] for point in telemetry_points]
signal_strengths = [point[2] for point in telemetry_points]

# Create a 2D scatter plot for Battery Level vs Radiation Level
fig = go.Figure()

# Add scatter plot for Battery Level vs Radiation Level
fig.add_trace(go.Scatter(
    x=battery_levels, 
    y=radiation_levels, 
    mode='lines+markers',
    marker=dict(size=10, color='green', opacity=0.8),
    name='Battery vs Radiation'
))

# Add another line for Battery Level vs Signal Strength
fig.add_trace(go.Scatter(
    x=battery_levels,
    y=signal_strengths,
    mode='lines+markers',
    marker=dict(size=10, color='blue', opacity=0.8),
    name='Battery vs Signal Strength'
))

# Add hover text for additional insights
hover_texts = [
    f"Battery: {bat}<br>Radiation: {rad}<br>Signal: {sig}"
    for bat, rad, sig in zip(battery_levels, radiation_levels, signal_strengths)
]
fig.data[0].text = hover_texts
fig.data[1].text = hover_texts

# Update layout with titles
fig.update_layout(
    title='2D Telemetry Data Visualization',
    xaxis_title='Battery Level',
    yaxis_title='Levels (Radiation and Signal)',
    hovermode="x unified",
    margin=dict(l=0, r=0, b=0, t=40),
    legend=dict(x=0.8, y=1)
)

# Show the 2D plot
fig.show()