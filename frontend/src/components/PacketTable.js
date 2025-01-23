import React from 'react';
import { Table } from 'antd';

const PacketTable = ({ packets }) => {
  const columns = [
    { title: 'Timestamp', dataIndex: 'timestamp' },
    { title: 'Source IP', dataIndex: 'source_ip' },
    { title: 'Destination IP', dataIndex: 'destination_ip' },
    { title: 'Protocol', dataIndex: 'protocol' }
  ];

  return (
    <Table 
      dataSource={packets} 
      columns={columns} 
      rowKey="id"
    />
  );
};

export default PacketTable;