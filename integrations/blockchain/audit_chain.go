package main

import (
	"crypto/sha256"
	"fmt"
	"time"
)

type Block struct {
	Timestamp     int64
	EventData     string
	PrevBlockHash []byte
	Hash          []byte
}

func (b *Block) SetHash() {
	headers := fmt.Sprintf("%d%s%x", b.Timestamp, b.EventData, b.PrevBlockHash)
	hash := sha256.Sum256([]byte(headers))
	b.Hash = hash[:]
}

func main() {
	fmt.Println("AIP-HSD Blockchain Audit Chain: Logging critical security event...")

	genesisBlock := Block{time.Now().Unix(), "GENESIS_EVENT: PLATFORM_BOOT", []byte{}, []byte{}}
	genesisBlock.SetHash()

	alertBlock := Block{time.Now().Unix(), "ALERT: RANSOMWARE_ALPHA_CORRELATED", genesisBlock.Hash, []byte{}}
	alertBlock.SetHash()

	fmt.Printf("Event: %s\nHash: %x\n", alertBlock.EventData, alertBlock.Hash)
	fmt.Println("Status: IMMUTABLE_AUDIT_LOG_COMMITTED")
}
