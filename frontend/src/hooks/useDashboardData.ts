import { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

export interface Threat {
  id: number;
  name: string;
  type: string;
  source: string;
  risk_score: number;
  location: string;
  description: string;
  timestamp: string;
}

export interface Device {
  id: number;
  ip_address: string;
  os: string;
  hostname: string;
  role: string;
  status: 'online' | 'offline' | 'vulnerable' | 'compromised';
  risk_score: number;
  last_scan: string;
}

export interface Alert {
  id: number;
  title: string;
  severity: string;
  message: string;
  device_id: number | null;
  timestamp: string;
}

export interface DashboardSummary {
  global_threat_level: number;
  internal_threat_level: number;
  network_health: number;
  active_alerts: number;
}

export interface DashboardData {
  threats: Threat[];
  devices: Device[];
  alerts: Alert[];
  summary: DashboardSummary;
  loading: boolean;
  error: string | null;
}

const useDashboardData = (): DashboardData => {
  const [data, setData] = useState<DashboardData>({
    threats: [],
    devices: [],
    alerts: [],
    summary: {
      global_threat_level: 0.85,
      internal_threat_level: 0.12,
      network_health: 0.99,
      active_alerts: 0
    },
    loading: true,
    error: null
  });

  const fetchData = async () => {
    try {
      const [threatsRes, devicesRes, alertsRes] = await Promise.all([
        axios.get(\`\${API_BASE_URL}/threats/\`),
        axios.get(\`\${API_BASE_URL}/devices/\`),
        axios.get(\`\${API_BASE_URL}/alerts/\`)
      ]);

      setData(prev => ({
        ...prev,
        threats: threatsRes.data,
        devices: devicesRes.data,
        alerts: alertsRes.data,
        summary: {
          ...prev.summary,
          active_alerts: alertsRes.data.length
        },
        loading: false,
        error: null
      }));
    } catch (err) {
      console.error('Failed to fetch dashboard data:', err);
      setData(prev => ({ ...prev, loading: false, error: 'Failed to sync with security backend' }));
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 15000);
    return () => clearInterval(interval);
  }, []);

  return data;
};

export default useDashboardData;
