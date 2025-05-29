package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Check RF signal stability
func checkRFStability() {
	signalStrength := rand.Float64() * 10 // Simulate signal strength between 0 and 10

	if signalStrength < 2 {
		fmt.Printf("RF Transmission Warning: Unstable signal! Strength: %.2f\n", signalStrength)
		attemptReconnection()
	} else {
		fmt.Printf("RF Transmission Stable: Signal Strength: %.2f\n", signalStrength)
	}
}

// Attempt reconnection if RF signal is weak
func attemptReconnection() {
	for attempt := 1; attempt <= 3; attempt++ { // Try 3 times to reconnect
		fmt.Printf("Attempting reconnection... Try %d\n", attempt)
		time.Sleep(1 * time.Second)
		if rand.Float64()*10 > 5 { // Random success rate
			fmt.Println("Reconnection successful!")
			return
		}
		fmt.Println("Reconnection failed.")
	}
	fmt.Println("Transmission failed after 3 attempts. Manual intervention needed.")
}

func main() {
	rand.Seed(time.Now().UnixNano())

	// Main loop to monitor RF signal stability
	for {
		checkRFStability()
		time.Sleep(1 * time.Second) // Check every 1 second
	}
}
