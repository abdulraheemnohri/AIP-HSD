import React from 'react';
import { Paper, Typography, List, ListItem, ListItemText, Divider, Button, Box } from '@mui/material';
import RadarIcon from '@mui/icons-material/Radar';

const ThreatHunterPanel = () => {
  const findings = [
    { id: 1, type: 'CORRELATED_THREAT', severity: 'CRITICAL', reason: "Global ransomware-alpha activity correlates with unusual outbound traffic on srv-db-03." },
    { id: 2, type: 'ANOMALY_PATTERN', severity: 'MEDIUM', reason: "Detected employee login latency pattern matching global phishing campaign TTPs." }
  ];

  return (
    <Paper sx={{ p: 2, borderLeft: '4px solid #FF1744' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h6"><RadarIcon sx={{ mr: 1, verticalAlign: 'middle' }} /> AI AUTONOMOUS THREAT HUNTER</Typography>
        <Button variant="outlined" color="primary" size="small">TRIGGER HUNT</Button>
      </Box>
      <List dense>
        {findings.map((f) => (
          <React.Fragment key={f.id}>
            <ListItem alignItems="flex-start" sx={{ px: 0 }}>
              <ListItemText
                primary={`${f.type} - ${f.severity}`}
                secondary={f.reason}
                primaryTypographyProps={{ color: f.severity === 'CRITICAL' ? 'secondary' : 'primary', variant: 'subtitle2' }}
              />
            </ListItem>
            <Divider component="li" />
          </React.Fragment>
        ))}
      </List>
    </Paper>
  );
};

export default ThreatHunterPanel;
