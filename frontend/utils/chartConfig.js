export const trafficChartConfig = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Network Traffic Analysis',
      },
    },
  };
  
  export const threatChartConfig = {
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'Threat Severity'
        }
      }
    }
  };