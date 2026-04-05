const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({
    query: req.query.query,
    tenant_id: "TENANT-NODE",
    external_intel: [{ title: "Node.js Search Result", url: "https://node.security.test" }],
    internal_context: [{ source: "Node Logs", match: "Found indicator in Express stream." }],
    timestamp: new Date()
  });
});

module.exports = router;
