import React from 'react';
import { Paper, Typography, Box, Switch, FormControlLabel, List, ListItem, ListItemText, Divider, Select, MenuItem, InputLabel, FormControl } from '@mui/material';

const SecuritySettings: React.FC = () => (
  <Paper sx={{ p: 3, bgcolor: '#1c2026', height: '100%' }}>
    <Typography variant="h6" gutterBottom color="primary">SYSTEM SECURITY POLICIES</Typography>
    <List>
      <ListItem sx={{ px: 0 }}>
        <FormControlLabel
          control={<Switch defaultChecked color="primary" />}
          label="Enable AI Autonomous Remediation"
        />
      </ListItem>
      <Divider />
      <ListItem sx={{ px: 0 }}>
        <FormControlLabel
          control={<Switch defaultChecked color="primary" />}
          label="Real-time OSINT Aggregation"
        />
      </ListItem>
      <Divider />
      <ListItem sx={{ px: 0 }}>
        <Box sx={{ width: '100%', mt: 2 }}>
          <FormControl fullWidth>
            <InputLabel id="rbac-role-label">Default RBAC Role</InputLabel>
            <Select
              labelId="rbac-role-label"
              id="rbac-role"
              value="Analyst"
              label="Default RBAC Role"
              sx={{ color: 'text.primary' }}
            >
              <MenuItem value="Admin">Admin</MenuItem>
              <MenuItem value="Analyst">Analyst</MenuItem>
              <MenuItem value="Executive">Executive</MenuItem>
            </Select>
          </FormControl>
        </Box>
      </ListItem>
      <Divider />
      <ListItem sx={{ px: 0 }}>
        <ListItemText
          primary="Audit Log Retention"
          secondary="Logs older than 90 days are automatically archived to the Ruby maintenance worker."
          primaryTypographyProps={{ variant: 'subtitle2' }}
        />
      </ListItem>
    </List>
  </Paper>
);

export default SecuritySettings;
