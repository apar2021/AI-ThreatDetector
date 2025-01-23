import sqlite3
from typing import List, Dict
from models.packet_model import PacketInfo

class DatabaseManager:
    def __init__(self, db_path='cybersecurity_packets.db'):
        self.db_path = db_path
        self._create_tables()

    def _create_tables(self):
        """Create necessary database tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS packets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME,
                    protocol TEXT,
                    source_ip TEXT,
                    destination_ip TEXT,
                    packet_length INTEGER
                )
            ''')
            conn.commit()

    def save_packets(self, packets: List[PacketInfo]):
        """Save packet information to database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            for packet in packets:
                cursor.execute('''
                    INSERT INTO packets 
                    (timestamp, protocol, source_ip, destination_ip, packet_length) 
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    packet.timestamp.isoformat(), 
                    packet.protocol, 
                    packet.source_ip, 
                    packet.destination_ip, 
                    packet.packet_length
                ))
            conn.commit()

    def get_recent_packets(self, limit: int = 1000):
        """Retrieve recent packets"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM packets 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (limit,))
            return cursor.fetchall()

# Singleton database manager
db_manager = DatabaseManager()