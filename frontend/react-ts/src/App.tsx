import React, { useState, useEffect } from 'react';
import { ThemeProvider, CssBaseline, Box, Grid, Container, Typography, AppBar, Toolbar, IconButton, Badge, LinearProgress, Alert, useMediaQuery } from '@mui/material';
import NotificationsIcon from '@mui/icons-material/Notifications';
import AccountCircle from '@mui/icons-material/AccountCircle';
import SettingsIcon from '@mui/icons-material/Settings';
import theme from './theme/theme';
import RiskCards from './components/RiskCards';
import ThreatMap from './components/ThreatMap';
import NetworkMap from './components/NetworkMap';
import AlertsFeed from './components/AlertsFeed';
import InsightsPanel from './components/InsightsPanel';
import ThreatHunterPanel from './components/ThreatHunterPanel';
import MalwareSandboxPanel from './components/MalwareSandboxPanel';
import ThreatCorrelationGraph from './components/ThreatCorrelationGraph';
import TrendChart from './components/TrendChart';
import SecuritySettings from './components/SecuritySettings';
import ThreeDSOC from './components/ThreeDSOC';
import WarRoomHITL from './components/WarRoomHITL';
import useDashboardData from './hooks/useDashboardData';

function App() {
  const { summary, alerts, loading, error } = useDashboardData();
  const [view, setView] = useState<'DASHBOARD' | 'SETTINGS'>('DASHBOARD');
  const isTablet = useMediaQuery(theme.breakpoints.between('md', 'lg'));

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh', bgcolor: 'background.default' }}>
        {loading && <LinearProgress color="primary" sx={{ position: 'fixed', top: 0, width: '100%', zIndex: 9999 }} />}

        <AppBar position="static" color="transparent" elevation={0} sx={{ borderBottom: '1px solid rgba(0, 229, 255, 0.2)' }}>
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1, color: 'primary.main', fontWeight: 'bold', letterSpacing: 2 }}>
              AIP-HSD // SENTINEL COMMAND
            </Typography>
            {error && <Alert severity="error" variant="outlined" sx={{ mr: 2, py: 0 }}>{error}</Alert>}
            <IconButton color="inherit" onClick={() => setView(view === 'DASHBOARD' ? 'SETTINGS' : 'DASHBOARD')}>
              <SettingsIcon />
            </IconButton>
            <IconButton color="inherit">
              <Badge badgeContent={alerts.length} color="error">
                <NotificationsIcon />
              </Badge>
            </IconButton>
            <IconButton color="inherit">
              <AccountCircle />
            </IconButton>
          </Toolbar>
        </AppBar>

        <Container maxWidth="xl" sx={{ mt: 4, mb: 4, flexGrow: 1 }}>
          {view === 'SETTINGS' ? (
            <SecuritySettings />
          ) : (
            <Grid container spacing={3}>
              <Grid item xs={12} lg={8}>
                <Grid container spacing={3}>
                  <Grid item xs={12}>
                    <ThreeDSOC />
                  </Grid>
                  <Grid item xs={12}>
                    <RiskCards summary={summary} />
                  </Grid>
                  <Grid item xs={12}>
                    <TrendChart />
                  </Grid>
                </Grid>
              </Grid>

              <Grid item xs={12} lg={4}>
                <Stack spacing={3}>
                  <WarRoomHITL />
                  <AlertsFeed alerts={alerts} />
                </Stack>
              </Grid>

              <Grid item xs={12} md={isTablet ? 12 : 6}>
                <ThreatHunterPanel />
              </Grid>
              <Grid item xs={12} md={isTablet ? 12 : 6}>
                <MalwareSandboxPanel />
              </Grid>

              <Grid item xs={12}>
                <ThreatCorrelationGraph />
              </Grid>

              <Grid item xs={12}>
                <NetworkMap />
              </Grid>

              <Grid item xs={12}>
                <InsightsPanel />
              </Grid>
            </Grid>
          )}
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App;
