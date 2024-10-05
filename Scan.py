import asyncio
from bleak import BleakScanner

async def scan_devices():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()
    for idx, device in enumerate(devices):
        print(f"[{idx}] {device.name} - {device.address}")

asyncio.run(scan_devices())
