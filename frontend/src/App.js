import React, { useState } from 'react';
import { ThemeProvider, CssBaseline, Box, Grid, Container, Typography, AppBar, Toolbar, IconButton, Badge } from '@mui/material';
import NotificationsIcon from '@mui/icons-material/Notifications';
import AccountCircle from '@mui/icons-material/AccountCircle';
import theme from './theme/theme';
import RiskCards from './components/RiskCards';
import ThreatMap from './components/ThreatMap';
import NetworkMap from './components/NetworkMap';
import AlertsFeed from './components/AlertsFeed';
import InsightsPanel from './components/InsightsPanel';
import ThreatHunterPanel from './components/ThreatHunterPanel';
import MalwareSandboxPanel from './components/MalwareSandboxPanel';

function App() {
  const [alerts] = useState([
    { id: 1, title: 'Unauthorized Access Attempt', severity: 'high', message: 'Targeted SQL injection attempt detected on srv-web-01.' },
    { id: 2, title: 'Unusual Outbound Traffic', severity: 'medium', message: 'High volume of encrypted data leaving workstation-DB37-B42 via non-standard port 8443.' },
  ]);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <AppBar position="static" color="transparent" elevation={0} sx={{ borderBottom: '1px solid rgba(255, 255, 255, 0.12)' }}>
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1, color: 'primary.main', fontWeight: 'bold' }}>
              AIP-HSD
            </Typography>
            <IconButton color="inherit">
              <Badge badgeContent={2} color="error">
                <NotificationsIcon />
              </Badge>
            </IconButton>
            <IconButton color="inherit">
              <AccountCircle />
            </IconButton>
          </Toolbar>
        </AppBar>

        <Container maxWidth="xl" sx={{ mt: 4, mb: 4, flexGrow: 1 }}>
          <Grid container spacing={3}>
            {/* Global Context & Map */}
            <Grid item xs={12} lg={8}>
              <Grid container spacing={3}>
                <Grid item xs={12}>
                  <ThreatMap />
                </Grid>
                <Grid item xs={12}>
                  <RiskCards />
                </Grid>
              </Grid>
            </Grid>

            {/* Sidebar Feed */}
            <Grid item xs={12} lg={4}>
              <AlertsFeed alerts={alerts} />
            </Grid>

            {/* Advanced AI Modules */}
            <Grid item xs={12} md={6}>
              <ThreatHunterPanel />
            </Grid>
            <Grid item xs={12} md={6}>
              <MalwareSandboxPanel />
            </Grid>

            {/* Internal Network Map */}
            <Grid item xs={12}>
              <NetworkMap />
            </Grid>

            {/* AI Insights Area */}
            <Grid item xs={12}>
              <InsightsPanel />
            </Grid>
          </Grid>
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App;
