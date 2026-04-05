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
				{"id": 301, "name": "Go-Exploit-Delta", "risk_score": 88.2, "type": "exploit", "timestamp": time.Now()},
			})
		})
		api.GET("/alerts", func(c *gin.Context) {
			c.JSON(http.StatusOK, []gin.H{
				{"id": 401, "title": "Go Alert: Kernel Anomaly", "severity": "critical", "timestamp": time.Now()},
			})
		})
		api.GET("/compliance/status", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{
				"standards": []gin.H{
					{"name": "ISO 27001", "status": "COMPLIANT", "score": 97.5},
				},
			})
		})
		api.GET("/search", func(c *gin.Context) {
			query := c.DefaultQuery("query", "")
			c.JSON(http.StatusOK, gin.H{
				"query": query,
				"results": []string{"Go internal hit 1", "Go internal hit 2"},
			})
		})
		api.GET("/settings", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{
				"enable_ai": true,
				"rbac": "Admin",
			})
		})
	}

	r.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"message": "AIP-HSD Go Universal API is live."})
	})

	r.Run(":8000")
}
