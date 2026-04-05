import React from 'react';
import { Paper, Typography, Box, List, ListItem, ListItemText, Button, Divider, Stack } from '@mui/material';
import GavelIcon from '@mui/icons-material/Gavel';

const WarRoomHITL: React.FC = () => {
  const pendingActions = [
    { id: 'ACT-001', threat: 'Ransomware-Alpha', action: 'ISOLATE_CLUSTER_4', priority: 'CRITICAL' },
    { id: 'ACT-002', threat: 'Credential-Spike', action: 'REVOKE_USER_ACCESS', priority: 'HIGH' }
  ];

  return (
    <Paper sx={{ p: 2, bgcolor: '#0a0e14', border: '1px solid #FF525F' }}>
      <Typography variant="h6" color="secondary" gutterBottom>
        <GavelIcon sx={{ mr: 1, verticalAlign: 'middle' }} /> WAR ROOM // HUMAN-IN-THE-LOOP (HITL)
      </Typography>
      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 2 }}>
        AUTHORIZATION REQUIRED FOR AI-SUGGESTED REMEDIATION
      </Typography>
      <List dense>
        {pendingActions.map((act) => (
          <React.Fragment key={act.id}>
            <ListItem sx={{ px: 0, flexDirection: 'column', alignItems: 'flex-start' }}>
              <ListItemText
                primary={\`\${act.threat} // \${act.action}\`}
                secondary={\`PRIORITY: \${act.priority}\`}
                primaryTypographyProps={{ color: 'primary', fontWeight: 'bold' }}
              />
              <Stack direction="row" spacing={1} sx={{ mt: 1 }}>
                <Button size="small" variant="contained" color="secondary">APPROVE</Button>
                <Button size="small" variant="outlined" sx={{ color: 'text.secondary', borderColor: 'text.secondary' }}>REJECT</Button>
              </Stack>
            </ListItem>
            <Divider sx={{ my: 1, bgcolor: 'rgba(255,255,255,0.1)' }} />
          </React.Fragment>
        ))}
      </List>
    </Paper>
  );
};

export default WarRoomHITL;
