FROM python:3.11-slim

COPY inventory_manager.py /usr/src/app/

# inventory.json is read/written here; mount a host folder on /data to keep it
WORKDIR /data
VOLUME /data

CMD ["python", "/usr/src/app/inventory_manager.py"]
