from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import pyshark
import json
from .models import Packet, SessionLocal
from .app.gpt_classifier import classify_packet_with_gpt

app = FastAPI()


def save_to_sqlite(data, db: Session):
    for packet in data:
        db.add(Packet(**packet))
    db.commit()

# Endpoint to upload PCAP file, parse it, and classify anomalies using GPT
@app.post("/upload_pcap/")
async def upload_pcap(file: UploadFile = File(...), save_as_json: bool = False):
    # Save the uploaded PCAP file
    pcap_path = f"/tmp/{file.filename}"
    with open(pcap_path, "wb") as buffer:
        buffer.write(await file.read())

    # Parse the PCAP file using PyShark
    packets = []
    try:
        cap = pyshark.FileCapture(pcap_path, only_summaries=True)
        for packet in cap:
            packet_description = f"Source IP: {packet.source}, Destination IP: {packet.destination}, Protocol: {packet.protocol}, Length: {packet.length}"
            anomaly_prediction = classify_packet_with_gpt(packet_description)
            
            # Store the packet data and GPT prediction
            packets.append({
                'timestamp': packet.sniff_time.isoformat(),
                'src_ip': packet.source,
                'dst_ip': packet.destination,
                'protocol': packet.protocol,
                'length': packet.length,
                'is_anomalous': 1 if anomaly_prediction == 'anomalous' else 0
            })
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing PCAP: {str(e)}")

    # Initialize the database session
    db = SessionLocal()

    # Save packet data to SQLite
    save_to_sqlite(packets, db)

    # Optionally save to JSON file
    if save_as_json:
        with open("traffic_data.json", "w") as json_file:
            json.dump(packets, json_file)

    return JSONResponse(content={"status": "success", "message": "Data processed successfully!"}, status_code=200)