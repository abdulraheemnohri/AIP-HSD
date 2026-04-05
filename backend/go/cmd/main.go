package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

func main() {
	r := gin.Default()

	api := r.Group("/api")
	{
		api.GET("/threats", func(c *gin.Context) {
			c.JSON(http.StatusOK, []gin.H{
				{
					"id": 301,
					"name": "Go-Exploit-Delta",
					"type": "exploit",
					"source": "CERT-GO",
					"risk_score": 88.2,
					"location": "Global",
					"description": "Go-based detection of delta exploit.",
					"timestamp": time.Now().Format(time.RFC3339),
				},
			})
		})
		api.GET("/alerts", func(c *gin.Context) {
			c.JSON(http.StatusOK, []gin.H{
				{
					"id": 401,
					"title": "Go Alert: Kernel Anomaly",
					"severity": "critical",
					"message": "High-severity anomaly detected via Go agent.",
					"device_id": 1,
					"tenant_id": "TENANT-GO",
					"timestamp": time.Now().Format(time.RFC3339),
				},
			})
		})
	}

	r.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"message": "AIP-HSD Go Universal API is live."})
	})

	r.Run(":8000")
}
