#!/usr/bin/env python3
import shutil

def check_disk(threshold=20):
    print("\n==== Disk Space Check ====")
    usage = shutil.disk_usage("/")
    print(f"Total: {usage.total/1024/1024:.2f} MB")
    print(f"Used: {usage.used/1024/1024:.2f} MB")
    print(f"Free: {usage.free/1024/1024:.2f} MB")
    
    if usage.free/usage.total*100 < threshold:
        print(f"⚠️ Warning: Only {usage.free/usage.total*100:.1f}% free space left!")

if __name__ == "__main__":
    check_disk()
