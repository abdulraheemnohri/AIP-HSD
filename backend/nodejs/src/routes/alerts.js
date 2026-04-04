const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json([
    { id: 201, title: "Node Alert: Unusual Traffic", severity: "high", message: "Detected on Segment 4", timestamp: new Date() }
  ]);
});

module.exports = router;
