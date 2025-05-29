// main.go
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"strings"
	"time"
)

// TelemetryData structure to hold telemetry information
type TelemetryData struct {
	BatteryLevel   int    json:"battery_level"
	RadiationLevel int    json:"radiation_level"
	SignalStrength int    json:"signal_strength"
	TransferStatus string json:"transfer_status"
}

// Generate random telemetry data
func generateTelemetryData() TelemetryData {
	rand.Seed(time.Now().UnixNano()) // Seed the random number generator

	// Generate telemetry data
	batteryLevel := rand.Intn(101)    // Battery level: 0 to 100
	radiationLevel := rand.Intn(1001) // Radiation level: 0 to 1000
	signalStrength := rand.Intn(26)   // Signal strength: 0 to 25 (for 25 tall lines)

	// Determine transfer status and anomalies
	transferStatus := "Data successfully reached at base station."
	if signalStrength < 5 { // Simulate an anomaly for low signal strength
		transferStatus = "Anomaly detected! Strength too low, attempting reconnection...........................................................................reconnecting...............enhancing the data.............................................................connection successfully permitted ..........................transmission code is upgraded"
	}

	return TelemetryData{
		BatteryLevel:   batteryLevel,
		RadiationLevel: radiationLevel,
		SignalStrength: signalStrength,
		TransferStatus: transferStatus,
	}
}

// Convert integer to binary string
func intToBinaryString(n int) string {
	return strconv.FormatInt(int64(n), 2)
}

// Draw a larger terminal-based graph for signal strength (25 tall, 20 wide)
func drawSignalStrengthGraph(strength int) {
	barHeight := 25 // Maximum height for the graph
	barWidth := 20  // Width of the graph

	fmt.Println("Signal Strength Graph:")
	for i := barHeight; i > 0; i-- {
		if strength >= i {
			fmt.Println("| " + strings.Repeat("#", barWidth)) // Filled line (represents signal strength)
		} else {
			fmt.Println("| " + strings.Repeat(" ", barWidth)) // Empty line
		}
	}
	fmt.Println("+" + strings.Repeat("-", barWidth+1))      // Bottom line of the graph
	fmt.Printf("Signal Strength.....: %d/25\n\n", strength) // Display numerical value
}

// Log telemetry data in normal and binary formats to the terminal
func logTelemetryData(data TelemetryData) {
	// Log normal data
	fmt.Println("Normal Telemetry Data:")
	fmt.Println("Battery Level........: ", data.BatteryLevel)
	fmt.Println("Radiation Level............: ", data.RadiationLevel)
	fmt.Println("Signal Strength.................: ", data.SignalStrength)
	fmt.Println("Transfer Status...........................: ", data.TransferStatus)
	fmt.Println("Analysing the data..................")
	fmt.Println("Encrypting the data...................................................................................")

	// Draw larger graph for signal strength
	drawSignalStrengthGraph(data.SignalStrength)

	// Log binary data
	fmt.Println("\nBinary Telemetry Data:")
	fmt.Println("Battery Level (Binary)....................: ", intToBinaryString(data.BatteryLevel))
	fmt.Println("Radiation Level (Binary).............................: ", intToBinaryString(data.RadiationLevel))
	fmt.Println("Signal Strength (Binary)......................................: ", intToBinaryString(data.SignalStrength))
	fmt.Println("\n-------------------------\n")
	fmt.Println("Data is coming in encrypted form and changing frequency in 0.00111 sec...........")
	fmt.Println("No anomalies detected. If detected, it will be shown at localhost.")
}

// Telemetry handler to respond to requests
func telemetryHandler(w http.ResponseWriter, r *http.Request) {
	data := generateTelemetryData() // Generate telemetry data

	// Log the telemetry data to the terminal in normal and binary format
	logTelemetryData(data)

	// Prepare response with both normal and binary representation
	response := map[string]interface{}{
		"normal": data,
		"binary": map[string]string{
			"battery_level":   intToBinaryString(data.BatteryLevel),
			"radiation_level": intToBinaryString(data.RadiationLevel),
			"signal_strength": intToBinaryString(data.SignalStrength),
		},
	}

	// Set content type and send response
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func main() {
	http.HandleFunc("/telemetry", telemetryHandler) // Define the route
	log.Println("Server starting on :8080...")
	err := http.ListenAndServe(":8080", nil) // Start the server on port 8080
	if err != nil {
		log.Fatal(err) // Panic if server fails to start
	}
}
