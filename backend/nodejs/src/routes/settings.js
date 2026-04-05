const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({
    enable_ai_remediation: true,
    realtime_osint: true,
    rbac_role_default: "Analyst"
  });
});

module.exports = router;
