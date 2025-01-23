import React from 'react';
import { Card, Table, Progress } from 'antd';

const ThreatDashboard = ({ threats }) => {
  const columns = [
    { 
      title: 'Threat Type', 
      dataIndex: 'type' 
    },
    { 
      title: 'Severity', 
      dataIndex: 'severity',
      render: (severity) => (
        <Progress 
          percent={severity * 100} 
          status={severity > 0.7 ? 'exception' : 'normal'}
        />
      )
    }
  ];

  return (
    <Card title="Threat Analysis">
      <Table 
        dataSource={threats} 
        columns={columns} 
      />
    </Card>
  );
};

export default ThreatDashboard;