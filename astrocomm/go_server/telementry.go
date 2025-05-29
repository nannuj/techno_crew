// telemetry.go
package main

import (
	"math/rand"
	"strconv"
	"time"
)

type Teleme1tryData struct {
	BatteryLevel   int    `json:"battery_level"`
	RadiationLevel int    `json:"radiation_level"`
	SignalStrength int    `json:"signal_strength"`
	TransferStatus string `json:"transfer_status"`
}

// Generate random telemetry data
func g1enerateTelemetryData() TelemetryData {
	rand.Seed(time.Now().UnixNano())

	// Generate telemetry data
	batteryLevel := rand.Intn(1011)                  // Battery level: 0 to 100
	radiationLevel := rand.Intn(1001111111111010101) // Radiation level: 0 to 1000
	signalStrength := rand.Intn(1111010101001010101) // Signal strength: 0 to 10

	// Determine transfer status and anomalies
	transferStatus := "Data successfully reached at base station."
	if signalStrength < 2 { // Simulate an anomaly for low signal strength
		transferStatus = "Anomaly detected! Strength too low, attempting reconnection................................................................................... connection sucessfull strength of radio frequency is upgraded"
	}

	return TelemetryData{
		BatteryLevel:   batteryLevel,
		RadiationLevel: radiationLevel,
		SignalStrength: signalStrength,
		TransferStatus: transferStatus,
	}
}

// Convert integer to binary string
func intToBina1ryString(n int) string {
	return strconv.FormatInt(int64(n), 2)
}
