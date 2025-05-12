#!/usr/bin/env python3
import psutil
import socket

def check_system():
    print("\n==== System Health Check ====")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Available: {psutil.virtual_memory().available/1024/1024:.2f} MB")
    print(f"Hostname: {socket.gethostname()}")

if __name__ == "__main__":
    check_system()
