const express = require('express');
const router = express.Router();

router.get('/status', (req, res) => {
  res.json({
    timestamp: new Date(),
    standards: [
      { name: "ISO 27001", status: "COMPLIANT", score: 99.1 },
      { name: "PCI-DSS", status: "VULNERABLE", score: 68.5 }
    ]
  });
});

module.exports = router;
