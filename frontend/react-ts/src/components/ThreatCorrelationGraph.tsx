import React, { useEffect, useRef } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import * as d3 from 'd3';

const ThreatCorrelationGraph: React.FC = () => {
  const svgRef = useRef<SVGSVGElement | null>(null);

  useEffect(() => {
    if (!svgRef.current) return;

    const width = 800;
    const height = 300;
    const svg = d3.select(svgRef.current)
      .attr('viewBox', \`0 0 \${width} \${height}\`)
      .style('background-color', '#0a0e14');

    svg.selectAll('*').remove();

    const data = {
      nodes: [
        { id: 'Ransomware-Alpha', type: 'Global Threat' },
        { id: 'Botnet-Delta', type: 'Global Threat' },
        { id: 'srv-web-01', type: 'Internal Device' },
        { id: 'srv-db-03', type: 'Internal Device' },
        { id: 'ws-admin-10', type: 'Internal Device' }
      ],
      links: [
        { source: 'Ransomware-Alpha', target: 'srv-web-01' },
        { source: 'Ransomware-Alpha', target: 'ws-admin-10' },
        { source: 'Botnet-Delta', target: 'srv-db-03' }
      ]
    };

    const simulation = d3.forceSimulation(data.nodes as any)
      .force('link', d3.forceLink(data.links).id((d: any) => d.id).distance(150))
      .force('charge', d3.forceManyBody().strength(-200))
      .force('center', d3.forceCenter(width / 2, height / 2));

    const link = svg.append('g')
      .attr('stroke', '#FF525F')
      .attr('stroke-opacity', 0.6)
      .attr('stroke-dasharray', '4,2')
      .selectAll('line')
      .data(data.links)
      .join('line')
      .attr('stroke-width', 1.5);

    const node = svg.append('g')
      .selectAll('circle')
      .data(data.nodes)
      .join('circle')
      .attr('r', 10)
      .attr('fill', (d: any) => d.type === 'Global Threat' ? '#FF1744' : '#00E5FF')
      .attr('stroke', '#0a0e14')
      .attr('stroke-width', 2);

    node.append('title').text((d: any) => \`\${d.id} (\${d.type})\`);

    svg.append('g')
      .selectAll('text')
      .data(data.nodes)
      .join('text')
      .attr('dx', 15)
      .attr('dy', 5)
      .attr('fill', '#bac9cc')
      .style('font-size', '10px')
      .style('font-weight', 'bold')
      .text((d: any) => d.id);

    simulation.on('tick', () => {
      link
        .attr('x1', (d: any) => d.source.x)
        .attr('y1', (d: any) => d.source.y)
        .attr('x2', (d: any) => d.target.x)
        .attr('y2', (d: any) => d.target.y);

      node
        .attr('cx', (d: any) => d.x)
        .attr('cy', (d: any) => d.y);

      svg.selectAll('text')
        .attr('x', (d: any) => d.x)
        .attr('y', (d: any) => d.y);
    });

  }, []);

  return (
    <Paper sx={{ p: 2, bgcolor: '#0a0e14', position: 'relative', minHeight: 300 }}>
      <Typography variant="overline" color="secondary" sx={{ fontWeight: 'bold' }}>
        AI THREAT CORRELATION GRAPH
      </Typography>
      <Box sx={{ display: 'flex', justifyContent: 'center' }}>
        <svg ref={svgRef} style={{ width: '100%', height: 'auto' }}></svg>
      </Box>
    </Paper>
  );
};

export default ThreatCorrelationGraph;
