# backend/utils/file_handler.py
import os
import tempfile
from fastapi import UploadFile
import asyncio

class FileHandler:
    @staticmethod
    async def save_uploaded_file(file: UploadFile, prefix: str = 'pcap_') -> str:
        try:
            # Create temporary file
            temp_file = tempfile.NamedTemporaryFile(
                delete=False, 
                prefix=prefix, 
                suffix='.pcap'
            )
            
            # Write file contents
            content = await file.read()
            temp_file.write(content)
            temp_file.close()
            
            return temp_file.name
        except Exception as e:
            raise RuntimeError(f"File saving error: {str(e)}")

    @staticmethod
    def cleanup_file(file_path: str):
        try:
            if os.path.exists(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"File cleanup error: {str(e)}")