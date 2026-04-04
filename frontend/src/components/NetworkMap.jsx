import React, { useEffect, useRef } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import * as d3 from 'd3';

const NetworkMap = () => {
  const svgRef = useRef();

  useEffect(() => {
    const width = 800;
    const height = 450;
    const svg = d3.select(svgRef.current)
      .attr('viewBox', \`0 0 \${width} \${height}\`)
      .style('background-color', '#0a0e14');

    // Mock internal network data
    const nodes = [
      { id: 'gateway', group: 1, label: 'Gateway' },
      { id: 'srv-web-01', group: 2, label: 'Web-01' },
      { id: 'srv-db-01', group: 2, label: 'DB-01' },
      { id: 'srv-app-01', group: 2, label: 'App-01' },
      { id: 'ws-admin-01', group: 3, label: 'Admin-01' },
      { id: 'ws-dev-01', group: 3, label: 'Dev-01' },
      { id: 'ws-dev-02', group: 3, label: 'Dev-02' }
    ];

    const links = [
      { source: 'gateway', target: 'srv-web-01' },
      { source: 'gateway', target: 'srv-db-01' },
      { source: 'gateway', target: 'srv-app-01' },
      { source: 'srv-app-01', target: 'srv-db-01' },
      { source: 'gateway', target: 'ws-admin-01' },
      { source: 'gateway', target: 'ws-dev-01' },
      { source: 'gateway', target: 'ws-dev-02' }
    ];

    const simulation = d3.forceSimulation(nodes)
      .force('link', d3.forceLink(links).id(d => d.id).distance(100))
      .force('charge', d3.forceManyBody().strength(-300))
      .force('center', d3.forceCenter(width / 2, height / 2));

    const link = svg.append('g')
      .attr('stroke', '#31353c')
      .attr('stroke-opacity', 0.6)
      .selectAll('line')
      .data(links)
      .join('line')
      .attr('stroke-width', 1);

    const node = svg.append('g')
      .attr('stroke', '#0a0e14')
      .attr('stroke-width', 1.5)
      .selectAll('circle')
      .data(nodes)
      .join('circle')
      .attr('r', 8)
      .attr('fill', d => d.id.startsWith('srv') ? '#FF525F' : (d.id === 'gateway' ? '#00E5FF' : '#bac9cc'))
      .call(d3.drag()
        .on('start', dragstarted)
        .on('drag', dragged)
        .on('end', dragended));

    node.append('title').text(d => d.label);

    svg.append('g')
      .selectAll('text')
      .data(nodes)
      .join('text')
      .attr('dx', 12)
      .attr('dy', 4)
      .attr('fill', '#bac9cc')
      .style('font-size', '10px')
      .text(d => d.label);

    simulation.on('tick', () => {
      link
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);

      node
        .attr('cx', d => d.x)
        .attr('cy', d => d.y);

      svg.selectAll('text')
        .attr('x', d => d.x)
        .attr('y', d => d.y);
    });

    function dragstarted(event) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      event.subject.fx = event.subject.x;
      event.subject.fy = event.subject.y;
    }

    function dragged(event) {
      event.subject.fx = event.x;
      event.subject.fy = event.y;
    }

    function dragended(event) {
      if (!event.active) simulation.alphaTarget(0);
      event.subject.fx = null;
      event.subject.fy = null;
    }

  }, []);

  return (
    <Paper sx={{ p: 2, bgcolor: '#0a0e14', position: 'relative', minHeight: 450 }}>
      <Typography variant="overline" color="primary" sx={{ position: 'absolute', top: 16, left: 16, fontWeight: 'bold' }}>
        INTERNAL NETWORK TOPOLOGY
      </Typography>
      <Box sx={{ display: 'flex', justifyContent: 'center' }}>
        <svg ref={svgRef} style={{ width: '100%', height: 'auto' }}></svg>
      </Box>
    </Paper>
  );
};

export default NetworkMap;
