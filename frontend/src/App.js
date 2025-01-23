import React, { useState } from 'react';
import PcapUpload from './components/PcapUpload';
import ThreatDashboard from './components/ThreatDashboard';
import NetworkGraph from './components/NetworkGraph';
import PacketTable from './components/PacketTable';
import apiService from './services/apiService';

function App() {
  const [analysisData, setAnalysisData] = useState(null);
  const [threats, setThreats] = useState([]);

  const handlePcapUpload = async (file) => {
    try {
      const data = await apiService.uploadPcapFile(file);
      setAnalysisData(data);
      
      // Analyze threats
      const threatAnalysis = await apiService.analyzeThreat(data);
      setThreats(threatAnalysis.threats);
    } catch (error) {
      console.error('Analysis Failed:', error);
    }
  };

  return (
    <div className="cybersecurity-dashboard">
      <h1>AI Cybersecurity Threat Detector</h1>
      <PcapUpload onUpload={handlePcapUpload} />
      
      {analysisData && (
        <>
          <NetworkGraph data={analysisData} />
          <ThreatDashboard threats={threats} />
          <PacketTable packets={analysisData.packets} />
        </>
      )}
    </div>
  );
}

export default App;