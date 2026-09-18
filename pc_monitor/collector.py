import psutil
from datetime import datetime

def collect_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory()
    disk_percent = psutil.disk_usage("C:/")

    timestamp = datetime.now().isoformat(timespec="seconds")

    return {
        "cpu_percent": cpu_percent,
        "ram_percent": ram_percent.percent,
        "disk_percent": disk_percent.percent,
        "timestamp": timestamp
    }

if __name__ == "__main__":
    print(collect_metrics())