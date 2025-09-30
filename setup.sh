#!/bin/bash

# Fouad Sploit - Setup Script
# This script prepares the tool for use

echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║                     FOUAD SPLOIT - BLACK HAT                          ║"
echo "║                         Setup Script                                  ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${YELLOW}[!] Not running as root. Some features may not work.${NC}"
    echo -e "${YELLOW}[!] Consider running: sudo ./setup.sh${NC}"
    echo ""
fi

echo -e "${CYAN}[*] Starting Fouad Sploit setup...${NC}"
echo ""

# Make main script executable
echo -e "${CYAN}[*] Making fouad_sploit.py executable...${NC}"
chmod +x fouad_sploit.py
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[+] fouad_sploit.py is now executable${NC}"
else
    echo -e "${RED}[-] Failed to make fouad_sploit.py executable${NC}"
    exit 1
fi

# Check Python version
echo ""
echo -e "${CYAN}[*] Checking Python version...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}[+] Python 3 found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}[-] Python 3 not found. Please install Python 3.6+${NC}"
    exit 1
fi

# Check Metasploit
echo ""
echo -e "${CYAN}[*] Checking Metasploit Framework...${NC}"
if command -v msfconsole &> /dev/null; then
    echo -e "${GREEN}[+] Metasploit Framework found${NC}"
    MSF_VERSION=$(msfconsole -v 2>&1 | head -n 1)
    echo -e "${GREEN}    $MSF_VERSION${NC}"
else
    echo -e "${YELLOW}[!] Metasploit Framework not found${NC}"
    echo -e "${YELLOW}[!] Install it from: https://www.metasploit.com/${NC}"
fi

# Create directories
echo ""
echo -e "${CYAN}[*] Creating project directories...${NC}"
mkdir -p results logs rc-files
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[+] Directories created: results/, logs/, rc-files/${NC}"
else
    echo -e "${YELLOW}[!] Could not create directories${NC}"
fi

# Set permissions
chmod 700 results logs rc-files 2>/dev/null

# Check for optional dependencies
echo ""
echo -e "${CYAN}[*] Checking optional dependencies...${NC}"

if python3 -c "import colorama" 2>/dev/null; then
    echo -e "${GREEN}[+] colorama installed${NC}"
else
    echo -e "${YELLOW}[!] colorama not installed (optional)${NC}"
    echo -e "${YELLOW}    Install with: pip3 install colorama${NC}"
fi

# Test installation
echo ""
echo -e "${CYAN}[*] Testing installation...${NC}"
if ./fouad_sploit.py --help > /dev/null 2>&1; then
    echo -e "${GREEN}[+] Fouad Sploit is working correctly!${NC}"
else
    echo -e "${RED}[-] Error testing Fouad Sploit${NC}"
    exit 1
fi

# Display network info
echo ""
echo -e "${CYAN}[*] Network Information:${NC}"
if command -v ip &> /dev/null; then
    MY_IP=$(ip route get 8.8.8.8 2>/dev/null | awk '{print $7; exit}')
    if [ -n "$MY_IP" ]; then
        echo -e "${GREEN}[+] Your IP address: $MY_IP${NC}"
    fi
fi

# Final message
echo ""
echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo -e "║                  ${GREEN}SETUP COMPLETED SUCCESSFULLY!${NC}                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}[+] Fouad Sploit is ready to use!${NC}"
echo ""
echo -e "${CYAN}Quick Start Commands:${NC}"
echo ""
echo -e "  ${YELLOW}Auto Mode (Recommended):${NC}"
echo -e "    ./fouad_sploit.py --auto --target <TARGET_IP>"
echo ""
echo -e "  ${YELLOW}Interactive Mode:${NC}"
echo -e "    ./fouad_sploit.py --interactive"
echo ""
echo -e "  ${YELLOW}Scan Mode:${NC}"
echo -e "    ./fouad_sploit.py --target <TARGET_IP> --scan"
echo ""
echo -e "  ${YELLOW}Help:${NC}"
echo -e "    ./fouad_sploit.py --help"
echo ""
echo -e "${CYAN}Documentation:${NC}"
echo -e "  - README.md        : Complete documentation"
echo -e "  - QUICKSTART.md    : Quick start guide"
echo -e "  - INSTALL.md       : Installation guide"
echo -e "  - CODE_EXAMPLES.md : Code examples"
echo ""
echo -e "${CYAN}Contact:${NC}"
echo -e "  📧 Email: zalaffouad37@gmail.com"
echo -e "  📱 Instagram: @1.pvl"
echo ""
echo -e "${YELLOW}⚠️  REMEMBER: Only use on authorized systems!${NC}"
echo ""
echo -e "${GREEN}Made with ❤️  by Fouad | © 2025${NC}"
echo ""
