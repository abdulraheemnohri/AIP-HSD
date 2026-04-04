package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"runtime"
	"time"
)

type SystemInfo struct {
	Hostname  string    \`json:"hostname"\`
	IPAddress string    \`json:"ip_address"\`
	OS        string    \`json:"os"\`
	Role      string    \`json:"role"\`
	LastScan  time.Time \`json:"last_scan"\`
	Status    string    \`json:"status"\`
}

func main() {
	hostname, _ := os.Hostname()
	info := SystemInfo{
		Hostname:  hostname,
		IPAddress: "127.0.0.1",
		OS:        fmt.Sprintf("%s %s", runtime.GOOS, runtime.GOARCH),
		Role:      "Endpoint",
		LastScan:  time.Now(),
		Status:    "online",
	}

	fmt.Printf("AIP-HSD Go Agent starting on %s (%s)...\n", info.Hostname, info.OS)

	payload, _ := json.MarshalIndent(info, "", "  ")
	fmt.Println("Telemetry Payload:")
	fmt.Println(string(payload))

	// In a real scenario, this would POST to /api/internal-status
	// http.Post("http://localhost:8000/api/internal-status", "application/json", bytes.NewBuffer(payload))
}
