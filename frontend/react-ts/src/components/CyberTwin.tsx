import React, { useEffect, useRef } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import HubIcon from '@mui/icons-material/Hub';

const CyberTwin: React.FC = () => {
  const mountRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    // In a real scenario, this would initialize a 3D digital twin
    // of the organizational infrastructure using Three.js and real-time telemetry.
    console.log("AIP-HSD Cyber-Twin 3D View initialized.");

    return () => {
      console.log("AIP-HSD Cyber-Twin 3D View disposed.");
    };
  }, []);

  return (
    <Paper sx={{ p: 2, bgcolor: '#0a0e14', position: 'relative', minHeight: 400, border: '1px solid #00E5FF' }}>
      <Typography variant="overline" color="primary" sx={{ fontWeight: 'bold' }}>
        <HubIcon sx={{ mr: 1, verticalAlign: 'middle' }} /> ORGANIZATIONAL CYBER-TWIN // 3D TOPOLOGY
      </Typography>
      <Box ref={mountRef} sx={{ width: '100%', height: 350, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <Typography variant="h5" color="text.secondary">[ 3D DIGITAL TWIN HUB // REAL-TIME MAPPING ]</Typography>
      </Box>
    </Paper>
  );
};

export default CyberTwin;

# Update App.tsx with CyberTwin
sed -i 's/import ThreeDSOC/import CyberTwin from ".\/components\/CyberTwin";\nimport ThreeDSOC/' /app/frontend/react-ts/src/App.tsx
sed -i 's/<ThreeDSOC \/>/<ThreeDSOC \/>\n                  <CyberTwin \/>/' /app/frontend/react-ts/src/App.tsx
