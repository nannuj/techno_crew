import time
import requests
import struct
import random

POINTS = ['A', 'B', 'C', 'D']

# Fetch binary telemetry data from the Go server
def fetch_telemetry():
    try:
        response = requests.get('http://localhost:8080/telemetry')
        if response.status_code == 200:
            return response.content
        else:
            print(f"Error: Failed to fetch telemetry, status code {response.status_code}")
    except Exception as e:
        print(f"Exception occurred: {e}")
    return None

# Decode binary telemetry data
def decode_telemetry(binary_data):
    telemetry = struct.unpack('>I d d d d d', binary_data)
    return {
        'Battery Level': telemetry[0],
        'Radiation Level': telemetry[1],
        'Signal Strength': telemetry[2],
        'Temperature': telemetry[3],
        'Velocity': telemetry[4],
        'Altitude': telemetry[5]
    }

# Simulate transmission through points A to D
def transmit_through_points(binary_data):
    for point in POINTS:
        print(f"Data received at Point {point} (Binary): {binary_data}")
        decoded_data = decode_telemetry(binary_data)
        print(f"Data at Point {point} (Decoded): {decoded_data}")
        check_for_errors(decoded_data, point)
        time.sleep(0.2)  # Simulate transmission delay between points

# Check for errors in telemetry data
def check_for_errors(telemetry, point):
    if telemetry['Battery Level'] < 20:
        print(f"Warning at Point {point}: Low battery!")
    if telemetry['Radiation Level'] > 80:
        print(f"Warning at Point {point}: High radiation level!")
    if telemetry['Signal Strength'] < 3:
        print(f"Warning at Point {point}: Weak signal strength!")
    print(f"Data successfully passed Point {point}")

# Main loop to fetch, transmit, and analyze telemetry data
if __name__ == "__main__":
    print("Taking data from virtual spacecraft...")
    
    binary_data = fetch_telemetry()  # Manual fetch, no auto-refresh
    
    if binary_data:
        print(f"Telemetry received in Binary: {binary_data}")
        transmit_through_points(binary_data)
    else:
        print("No telemetry data fetched. Please try again.")
def resolve_error():
    time.sleep(1)  # Simulate processing delay
    success_rate = 0.99
    if random.random() < success_rate:
        return "ML Model: Error resolved with 99% accuracy."
    else:
        return "ML Model: Failed to resolve the error."

if __name__ == "__main__":
    result = resolve_error()
    print(result)