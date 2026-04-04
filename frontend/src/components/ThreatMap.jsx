import React, { useEffect, useRef } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import * as d3 from 'd3';

const ThreatMap = () => {
  const svgRef = useRef();

  useEffect(() => {
    const width = 800;
    const height = 450;
    const svg = d3.select(svgRef.current)
      .attr('viewBox', \`0 0 \${width} \${height}\`)
      .style('background-color', '#0a0e14');

    const projection = d3.geoMercator()
      .scale(120)
      .translate([width / 2, height / 1.5]);

    const path = d3.geoPath().projection(projection);

    // Mock world map data (Simplified)
    d3.json('https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson').then(data => {
      svg.append('g')
        .selectAll('path')
        .data(data.features)
        .enter()
        .append('path')
        .attr('d', path)
        .attr('fill', '#1c2026')
        .attr('stroke', '#31353c')
        .attr('stroke-width', 0.5);

      // Mock threat hotspots
      const hotspots = [
        { name: 'USA', coords: [-77, 38], severity: 'HIGH' },
        { name: 'China', coords: [116, 39], severity: 'CRITICAL' },
        { name: 'Russia', coords: [37, 55], severity: 'MEDIUM' },
        { name: 'Germany', coords: [13, 52], severity: 'LOW' }
      ];

      svg.selectAll('circle')
        .data(hotspots)
        .enter()
        .append('circle')
        .attr('cx', d => projection(d.coords)[0])
        .attr('cy', d => projection(d.coords)[1])
        .attr('r', d => d.severity === 'CRITICAL' ? 8 : 4)
        .attr('fill', d => d.severity === 'CRITICAL' ? '#FF1744' : (d.severity === 'HIGH' ? '#FF525F' : '#00E5FF'))
        .attr('opacity', 0.8)
        .append('title')
        .text(d => \`THREAT: \${d.name} - \${d.severity}\`);
    });

  }, []);

  return (
    <Paper sx={{ p: 2, bgcolor: '#0a0e14', position: 'relative', minHeight: 450 }}>
      <Typography variant="overline" color="primary" sx={{ position: 'absolute', top: 16, left: 16, fontWeight: 'bold' }}>
        GLOBAL THREAT ARCHITECTURE
      </Typography>
      <Box sx={{ display: 'flex', justifyContent: 'center' }}>
        <svg ref={svgRef} style={{ width: '100%', height: 'auto' }}></svg>
      </Box>
    </Paper>
  );
};

export default ThreatMap;
