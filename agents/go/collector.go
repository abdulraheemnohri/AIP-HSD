package main

import (
	"encoding/json"
	"fmt"
	"os"
	"runtime"
	"time"
)

type Event struct {
	EventID     string \`json:"event_id"\`
	SourceAgent string \`json:"source_agent"\`
	EventType   string \`json:"event_type"\`
	Severity    string \`json:"severity"\`
	Payload     struct {
		Hostname         string    \`json:"hostname"\`
		IPAddress        string    \`json:"ip_address"\`
		Message          string    \`json:"message"\`
		ScreenResolution string    \`json:"screen_resolution"\` // Added display telemetry
		Timestamp        time.Time \`json:"timestamp"\`
	} \`json:"payload"\`
}

func main() {
	hostname, _ := os.Hostname()
	event := Event{
		EventID:     "EVT-GO-001",
		SourceAgent: "GO_COLLECTOR",
		EventType:   "TELEMETRY",
		Severity:    "LOW",
	}
	event.Payload.Hostname = hostname
	event.Payload.IPAddress = "127.0.0.1"
	event.Payload.Message = fmt.Sprintf("System Status: %s %s", runtime.GOOS, runtime.GOARCH)
	event.Payload.ScreenResolution = "2048x1536 (Tablet)" // Simulating tablet
	event.Payload.Timestamp = time.Now()

	fmt.Printf("AIP-HSD Go Agent: Emitting Unified Event with Display Telemetry...\n")
	payload, _ := json.MarshalIndent(event, "", "  ")
	fmt.Println(string(payload))
}
