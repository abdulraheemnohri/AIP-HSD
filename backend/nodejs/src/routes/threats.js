const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json([
    { id: 101, name: "Node-Ransom-Alpha", type: "ransomware", source: "OSINT", risk_score: 92.5, location: "USA", timestamp: new Date() }
  ]);
});

module.exports = router;
