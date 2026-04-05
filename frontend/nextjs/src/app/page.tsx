import React from 'react';
import { Box, Typography, Container, Grid, Stack, Paper, AppBar, Toolbar, IconButton, Badge } from '@mui/material';
import NotificationsIcon from '@mui/icons-material/Notifications';

export default function Home() {
  return (
    <Box sx={{ bgcolor: '#10141a', minHeight: '100vh', color: '#dfe2eb' }}>
      <AppBar position="static" color="transparent" elevation={0} sx={{ borderBottom: '1px solid rgba(0, 229, 255, 0.2)' }}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1, color: '#00E5FF', fontWeight: 'bold' }}>
            AIP-HSD // NEXT.JS SENTINEL
          </Typography>
          <IconButton color="inherit">
            <Badge badgeContent={5} color="error">
              <NotificationsIcon />
            </Badge>
          </IconButton>
        </Toolbar>
      </AppBar>

      <Container maxWidth="xl" sx={{ mt: 4 }}>
        <Grid container spacing={3}>
          <Grid item xs={12} lg={8}>
            <Paper sx={{ p: 4, bgcolor: '#1c2026', border: '1px solid #00E5FF' }}>
              <Typography variant="h4" color="primary">ACTIVE THREAT ARCHITECTURE</Typography>
              <Box sx={{ mt: 2, height: 300, bgcolor: '#0a0e14', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <Typography color="textSecondary">[ D3.JS WORLD MAP VISUALIZATION ]</Typography>
              </Box>
            </Paper>
          </Grid>
          <Grid item xs={12} lg={4}>
            <Paper sx={{ p: 2, bgcolor: '#0a0e14', border: '1px solid #FF525F' }}>
              <Typography variant="h6" color="secondary">WAR ROOM // HITL</Typography>
              <Typography variant="caption" color="textSecondary">PENDING AI AUTHORIZATIONS</Typography>
            </Paper>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
}
