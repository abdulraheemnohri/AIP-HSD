import React, { useEffect, useRef } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import * as d3 from 'd3';

const TrendChart: React.FC = () => {
  const svgRef = useRef<SVGSVGElement | null>(null);

  useEffect(() => {
    if (!svgRef.current) return;

    const width = 800;
    const height = 300;
    const margin = { top: 20, right: 30, bottom: 40, left: 50 };

    const svg = d3.select(svgRef.current)
      .attr('viewBox', \`0 0 \${width} \${height}\`)
      .style('background-color', '#0a0e14');

    svg.selectAll('*').remove();

    // Mock trend data
    const data = [
      { date: new Date(2024, 0, 1), threats: 10, anomalies: 5 },
      { date: new Date(2024, 1, 1), threats: 25, anomalies: 12 },
      { date: new Date(2024, 2, 1), threats: 15, anomalies: 8 },
      { date: new Date(2024, 3, 1), threats: 45, anomalies: 22 },
      { date: new Date(2024, 4, 1), threats: 35, anomalies: 18 }
    ];

    const x = d3.scaleTime()
      .domain(d3.extent(data, d => d.date) as [Date, Date])
      .range([margin.left, width - margin.right]);

    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => Math.max(d.threats, d.anomalies)) as number + 10])
      .nice()
      .range([height - margin.bottom, margin.top]);

    svg.append('g')
      .attr('transform', \`translate(0,\${height - margin.bottom})\`)
      .call(d3.axisBottom(x).ticks(5).tickSizeOuter(0))
      .attr('color', '#bac9cc');

    svg.append('g')
      .attr('transform', \`translate(\${margin.left},0)\`)
      .call(d3.axisLeft(y))
      .attr('color', '#bac9cc');

    const lineThreats = d3.line<any>()
      .x(d => x(d.date))
      .y(d => y(d.threats))
      .curve(d3.curveMonotoneX);

    const lineAnomalies = d3.line<any>()
      .x(d => x(d.date))
      .y(d => y(d.anomalies))
      .curve(d3.curveMonotoneX);

    svg.append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', '#FF1744')
      .attr('stroke-width', 2)
      .attr('d', lineThreats);

    svg.append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', '#00E5FF')
      .attr('stroke-width', 2)
      .attr('d', lineAnomalies);

  }, []);

  return (
    <Paper sx={{ p: 2, bgcolor: '#0a0e14', position: 'relative', minHeight: 300 }}>
      <Typography variant="overline" color="primary" sx={{ fontWeight: 'bold' }}>
        HISTORICAL THREAT TRENDS (90 DAYS)
      </Typography>
      <Box sx={{ display: 'flex', justifyContent: 'center' }}>
        <svg ref={svgRef} style={{ width: '100%', height: 'auto' }}></svg>
      </Box>
    </Paper>
  );
};

export default TrendChart;
