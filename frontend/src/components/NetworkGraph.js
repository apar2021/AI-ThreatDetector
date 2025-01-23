import React from 'react';
import { Network } from 'vis-network';

const NetworkGraph = ({ data }) => {
  const networkRef = React.useRef(null);

  React.useEffect(() => {
    // Create network visualization of packet flows
    const network = new Network(
      networkRef.current, 
      transformDataForVisualization(data)
    );
  }, [data]);

  return <div ref={networkRef} />;
};

export default NetworkGraph;