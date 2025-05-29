// Three.js 3D scene setup
let scene, camera, renderer;
let points = [];
let signalStrength = 10;

function init() {
  // Scene setup
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  renderer = new THREE.WebGLRenderer();
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  // Add ambient light
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
  scene.add(ambientLight);

  // Add directional light
  const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
  directionalLight.position.set(1, 1, 1).normalize();
  scene.add(directionalLight);

  // Add Grid Helper
  const gridHelper = new THREE.GridHelper(200, 50);
  scene.add(gridHelper);

  // Add Axis Helper
  const axesHelper = new THREE.AxesHelper(100);
  scene.add(axesHelper);

  // Set initial camera position
  camera.position.z = 100;

  // Fetch telemetry data from Go server and update the 3D visualization
  fetchTelemetryData();
}

// Fetch telemetry data from Go server
function fetchTelemetryData() {
  fetch('http://localhost:8080/telemetry')
    .then(response => response.json())
    .then(data => {
      updateData(data.normal); // Use the 'normal' data
    })
    .catch(error => console.error('Error fetching telemetry data:', error));
}

function updateData(telemetry) {
  // Clear existing points
  for (let i = 0; i < points.length; i++) {
    scene.remove(points[i]);
  }
  points = [];

  // Create a 3D cube for the telemetry data point
  const geometry = new THREE.BoxGeometry(5, 5, 5);
  const material = new THREE.MeshStandardMaterial({ color: getColorBasedOnSignal(telemetry.signal_strength) });
  const cube = new THREE.Mesh(geometry, material);

  // Set cube position based on telemetry data
  cube.position.set(
    telemetry.battery_level - 50, // Center around 0 for battery level
    telemetry.radiation_level / 10 - 50, // Scale radiation for visibility
    telemetry.signal_strength * 2 - 50 // Adjust signal strength scale
  );

  // Add cube to the scene
  scene.add(cube);
  points.push(cube);
}

// Determine color based on signal strength
function getColorBasedOnSignal(signal) {
  if (signal < 5) return 0xff0000; // Red for low signal
  else if (signal < 15) return 0xffff00; // Yellow for medium signal
  else return 0x00ff00; // Green for strong signal
}

function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}

// Resize the scene on window resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Initialize and animate the scene
init();
animate();
