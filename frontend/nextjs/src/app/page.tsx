import React from 'react';
import { Box, Typography, Container, Grid } from '@mui/material';

export default function Home() {
  return (
    <Container maxWidth="xl" sx={{ mt: 8 }}>
      <Box sx={{ p: 4, bgcolor: '#1c2026', border: '1px solid #00E5FF' }}>
        <Typography variant="h3" color="primary" gutterBottom>AIP-HSD // NEXT.JS EDITION</Typography>
        <Typography variant="h6" color="text.secondary">Universal Intelligence Dashboard - Active Sentinel</Typography>

        <Grid container spacing={4} sx={{ mt: 4 }}>
          <Grid item xs={12} md={4}>
            <Box sx={{ p: 2, borderLeft: '4px solid #FF1744', bgcolor: '#0a0e14' }}>
              <Typography variant="overline">GLOBAL THREAT LEVEL</Typography>
              <Typography variant="h4" color="secondary">CRITICAL</Typography>
            </Box>
          </Grid>
          {/* Add more Next.js components here */}
        </Grid>
      </Box>
    </Container>
  );
}
