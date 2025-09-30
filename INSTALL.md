# 📦 Fouad Sploit - Installation Guide

## Quick Installation (30 Seconds)

### For Kali Linux / Linux

```bash
# Navigate to the directory
cd "/home/kali/Desktop/New Folder 2"

# Make executable
chmod +x fouad_sploit.py

# Test installation
./fouad_sploit.py --help

# Run your first exploit
./fouad_sploit.py --auto --target <TARGET_IP>
```

That's it! You're ready to go! 🚀

## Detailed Installation Steps

### 1. System Requirements Check

```bash
# Check Python version (needs 3.6+)
python3 --version

# Check if Metasploit is installed
which msfconsole

# Check if running as root (recommended)
whoami
```

### 2. Download Fouad Sploit

#### Option A: Git Clone (Recommended)
```bash
git clone https://github.com/fouad/fouad-sploit.git
cd fouad-sploit
```

#### Option B: Manual Download
- Download the ZIP from GitHub
- Extract to your desired location
- Navigate to the folder

### 3. Set Permissions

```bash
# Make script executable
chmod +x fouad_sploit.py

# Verify permissions
ls -la fouad_sploit.py
```

### 4. Verify Installation

```bash
# Display help
./fouad_sploit.py --help

# Should display:
# ╔═══════════════════════════════════════════════╗
# ║        FOUAD SPLOIT - BLACK HAT               ║
# ╚═══════════════════════════════════════════════╝
```

## Install Metasploit Framework

### Kali Linux (Pre-installed)
```bash
# Update Metasploit
sudo msfupdate

# Start Metasploit
msfconsole
```

### Ubuntu/Debian
```bash
# Download installer
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall

# Make executable
chmod 755 msfinstall

# Run installer
sudo ./msfinstall

# Verify installation
msfconsole -v
```

### macOS
```bash
# Install via Homebrew
brew install metasploit

# Or download from official site
# https://www.metasploit.com/download
```

## Optional Dependencies

### Python Packages (Optional)
```bash
# For enhanced features
pip3 install colorama python-nmap

# Or install all at once
pip3 install -r requirements.txt
```

### Additional Tools (Recommended)
```bash
# Nmap for scanning
sudo apt-get install nmap

# Netcat for listeners
sudo apt-get install netcat

# Tmux for session management
sudo apt-get install tmux
```

## Configuration

### 1. Network Configuration

```bash
# Find your IP address
ip addr show
# or
ifconfig

# Test connectivity
ping -c 3 192.168.1.1
```

### 2. Firewall Configuration

```bash
# Allow incoming connections (for reverse shells)
sudo ufw allow 4444/tcp
sudo ufw allow 4445/tcp

# Check firewall status
sudo ufw status
```

### 3. Environment Variables (Optional)

```bash
# Add to ~/.bashrc or ~/.zshrc
export FOUAD_SPLOIT_PATH="/path/to/fouad-sploit"
export PATH="$PATH:$FOUAD_SPLOIT_PATH"

# Reload shell
source ~/.bashrc
```

## Post-Installation Setup

### Create Workspace

```bash
# Create results directory
mkdir -p results
mkdir -p logs
mkdir -p rc-files

# Set permissions
chmod 700 results logs rc-files
```

### First Run Test

```bash
# Test with localhost (safe)
./fouad_sploit.py --interactive

# When prompted:
# Target: 127.0.0.1
# Auto-detect ports: n
# Port: 445
# Follow the prompts...
```

## Docker Installation (Alternative)

### Build Docker Image

```bash
# Create Dockerfile (see CODE_EXAMPLES.md)
docker build -t fouad-sploit:latest .

# Run container
docker run -it --rm --network host fouad-sploit:latest --help
```

### Docker Compose

```bash
# Create docker-compose.yml
# (see CODE_EXAMPLES.md for full config)

# Start service
docker-compose up

# Run exploit
docker-compose run fouad-sploit --auto --target 192.168.1.100
```

## Troubleshooting

### Issue: "Permission Denied"

```bash
# Solution 1: Fix permissions
chmod +x fouad_sploit.py

# Solution 2: Run with Python directly
python3 fouad_sploit.py --help

# Solution 3: Run as root
sudo ./fouad_sploit.py --help
```

### Issue: "msfconsole not found"

```bash
# Install Metasploit Framework
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
sudo ./msfinstall

# Add to PATH
export PATH=$PATH:/opt/metasploit-framework/bin
```

### Issue: "No module named 'colorama'"

```bash
# Install Python dependencies
pip3 install colorama

# Or use system colors (works without colorama)
./fouad_sploit.py --help
```

### Issue: "Connection refused" or "No route to host"

```bash
# Check network connectivity
ping TARGET_IP

# Check if target is up
nmap -sn TARGET_IP

# Check firewall
sudo ufw status

# Check routing
ip route show
```

### Issue: "Exploit failed"

```bash
# Verify target is vulnerable
nmap -sV -p PORT TARGET_IP

# Try different exploit
./fouad_sploit.py --interactive
# Then manually select different exploit

# Check Metasploit logs
cat ~/.msf4/logs/framework.log
```

## Updating Fouad Sploit

### Git Method

```bash
cd /path/to/fouad-sploit
git pull origin main
chmod +x fouad_sploit.py
```

### Manual Method

```bash
# Download latest version
# Replace old files
# Preserve your configs and results
```

## Uninstallation

```bash
# Remove Fouad Sploit
cd ..
rm -rf fouad-sploit

# Remove configurations (optional)
rm -rf ~/.fouad-sploit

# Remove Docker images (if used)
docker rmi fouad-sploit:latest
```

## Security Notes

⚠️ **IMPORTANT:**
- Only use on authorized systems
- Keep Metasploit Framework updated
- Use strong passwords
- Secure your listener ports
- Don't expose to untrusted networks

## Support

If you encounter issues:

📧 **Email:** zalaffouad37@gmail.com  
📱 **Instagram:** [@1.pvl](https://instagram.com/1.pvl)

## System Compatibility

✅ **Tested On:**
- Kali Linux 2024.x
- Ubuntu 20.04/22.04
- Debian 11/12
- Parrot Security OS
- BlackArch Linux

✅ **Python Versions:**
- Python 3.6
- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10+

✅ **Metasploit Versions:**
- Metasploit 6.x
- Metasploit 5.x (legacy)

## Next Steps

After installation:

1. Read [README.md](README.md) for full documentation
2. Check [QUICKSTART.md](QUICKSTART.md) for quick commands
3. Review [CODE_EXAMPLES.md](CODE_EXAMPLES.md) for advanced usage
4. Join the community and contribute!

---

**Made with ❤️ by Fouad**  
**© 2025 Fouad. All Rights Reserved.**

📧 zalaffouad37@gmail.com | 📱 [@1.pvl](https://instagram.com/1.pvl)
