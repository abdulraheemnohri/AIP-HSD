const express = require('express');
const cors = require('cors');
const threatsRouter = require('./routes/threats');
const alertsRouter = require('./routes/alerts');
const complianceRouter = require('./routes/compliance');
const aiRouter = require('./routes/ai');

const app = express();
app.use(cors());
app.use(express.json());

app.use('/api/threats', threatsRouter);
app.use('/api/alerts', alertsRouter);
app.use('/api/compliance', complianceRouter);
app.use('/api/ai', aiRouter);

app.get('/', (req, res) => {
  res.json({ message: "AIP-HSD Node.js Universal API is live." });
});

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(\`Node.js Backend running on port \${PORT}\`);
});
