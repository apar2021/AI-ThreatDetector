import React, { useState } from 'react';
import { Button, Upload, message } from 'antd';
import { UploadOutlined } from '@ant-design/icons';

const PcapUpload = ({ onUpload }) => {
  const [fileList, setFileList] = useState([]);

  const handleUpload = async (options) => {
    const { file } = options;
    
    try {
      await onUpload(file);
      message.success(`${file.name} file uploaded successfully`);
      setFileList([{ ...file, status: 'done' }]);
    } catch (error) {
      message.error(`${file.name} file upload failed`);
      setFileList([{ ...file, status: 'error' }]);
    }
  };

  const uploadProps = {
    accept: '.pcap,.pcapng',
    multiple: false,
    onChange: (info) => setFileList(info.fileList),
    customRequest: handleUpload,
    fileList,
  };

  return (
    <Upload {...uploadProps}>
      <Button icon={<UploadOutlined />}>Upload PCAP File</Button>
    </Upload>
  );
};

export default PcapUpload;