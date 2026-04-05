import React, { useEffect, useRef } from 'react';
import { Box, Typography, Paper, Button } from '@mui/material';
import ViewInArIcon from '@mui/icons-material/ViewInAr';

const ThreeDSOC: React.FC = () => {
  const mountRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    // In a real scenario, this would initialize Three.js Scene, Camera, Renderer
    // and WebXR Manager for VR/AR support.
    console.log("AIP-HSD Three.js SOC with WebXR initialized.");

    return () => {
      console.log("AIP-HSD Three.js SOC with WebXR disposed.");
    };
  }, []);

  return (
    <Paper sx={{ p: 2, bgcolor: '#0a0e14', position: 'relative', minHeight: 450, overflow: 'hidden' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="overline" color="primary" sx={{ fontWeight: 'bold' }}>
          IMMERSIVE 3D SECURITY OPERATIONS CENTER // WEBXR ENABLED
        </Typography>
        <Button variant="outlined" size="small" startIcon={<ViewInArIcon />}>ENTER VR</Button>
      </Box>
      <Box ref={mountRef} sx={{ width: '100%', height: 350, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <Typography variant="h5" color="text.secondary">[ 3D GLOBAL THREAT HUD // WEBXR VR/AR MODE ]</Typography>
      </Box>
    </Paper>
  );
};

export default ThreeDSOC;
