# backend/services/threat_detection.py
import openai
from typing import Dict, Any, List

def analyze_threats(pcap_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    # Basic threat detection heuristics
    suspicious_activities = []
    
    # Check for potential threats based on protocols and traffic patterns
    for protocol, count in pcap_data['protocol_distribution'].items():
        if protocol in ['TCP', 'UDP'] and count > 1000:
            suspicious_activities.append({
                'type': 'High Volume Protocol Traffic',
                'protocol': protocol,
                'count': count
            })
    
    # Use GPT for advanced threat analysis
    try:
        gpt_analysis = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "system",
                "content": f"Analyze network traffic for potential security threats. Data: {pcap_data}"
            }]
        )
        
        # Extract insights from GPT response
        gpt_insights = gpt_analysis.choices[0].message.content
        
        suspicious_activities.append({
            'type': 'GPT Threat Analysis',
            'details': gpt_insights
        })
    except Exception as e:
        print(f"GPT Analysis Error: {e}")
    
    return suspicious_activities