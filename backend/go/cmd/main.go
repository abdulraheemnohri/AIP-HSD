package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	api := r.Group("/api")
	{
		api.GET("/threats", func(c *gin.Context) {
			c.JSON(http.StatusOK, []gin.H{
				{"id": 301, "name": "Go-Exploit-Delta", "risk_score": 88.2, "type": "exploit"},
			})
		})
		api.GET("/alerts", func(c *gin.Context) {
			c.JSON(http.StatusOK, []gin.H{
				{"id": 401, "title": "Go Alert: Kernel Anomaly", "severity": "critical"},
			})
		})
	}

	r.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"message": "AIP-HSD Go Universal API is live."})
	})

	r.Run(":8000")
}
