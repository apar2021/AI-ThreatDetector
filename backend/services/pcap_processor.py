from database.connection import db_manager

async def process_pcap(file: UploadFile) -> Dict[str, Any]:
    # Existing processing logic
    
    # Save packets to database
    packet_models = [
        PacketInfo(**{
            'timestamp': datetime.fromtimestamp(packet['timestamp']),
            'protocol': packet['protocol'],
            'source_ip': packet['source_ip'],
            'destination_ip': packet['dest_ip'],
            'packet_length': packet['packet_length']
        }) for packet in packet_details
    ]
    
    db_manager.save_packets(packet_models)
    db_manager.save_network_analysis({
        'total_packets': len(packet_details),
        'unique_protocols': list(set(p['protocol'] for p in packet_details)),
        'anomaly_score': calculate_anomaly_score()
    })
    
    return analysis_result