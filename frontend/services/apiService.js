import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api';

const apiService = {
  uploadPcapFile: async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`${API_BASE_URL}/upload-pcap`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      return response.data;
    } catch (error) {
      console.error('PCAP Upload Error:', error);
      throw error;
    }
  },

  fetchPacketHistory: async (limit = 1000) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/packet-history?limit=${limit}`);
      return response.data;
    } catch (error) {
      console.error('Packet History Error:', error);
      throw error;
    }
  },

  analyzeThreat: async (packetData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/analyze-threat`, packetData);
      return response.data;
    } catch (error) {
      console.error('Threat Analysis Error:', error);
      throw error;
    }
  }
};

export default apiService;