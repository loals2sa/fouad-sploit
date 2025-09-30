# 🤝 Contributing to Fouad Sploit

Thank you for considering contributing to **Fouad Sploit - Black Hat**! 

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Submitting Changes](#submitting-changes)
- [Style Guidelines](#style-guidelines)
- [Contact](#contact)

## 📜 Code of Conduct

This project follows ethical hacking principles:

- ✅ Only contribute features for **authorized penetration testing**
- ✅ Maintain **responsible disclosure** practices
- ✅ Respect **privacy and security**
- ❌ No malicious features
- ❌ No illegal activities

## 🎯 How Can I Contribute?

### Reporting Bugs

1. Check if the bug is already reported in [Issues](https://github.com/fouad/fouad-sploit/issues)
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version, etc.)
   - Screenshots if applicable

### Suggesting Features

1. Check existing feature requests
2. Create a new issue with `[Feature Request]` prefix
3. Explain:
   - What problem it solves
   - How it should work
   - Any security implications

### Adding Exploit Modules

```python
# Example: Adding new exploit suggestion
def get_exploit_modules():
    return {
        'service_name': [
            'exploit/path/to/module',
            'exploit/another/module',
        ],
    }
```

### Improving Documentation

- Fix typos
- Add examples
- Clarify instructions
- Translate to other languages

## 💻 Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/fouad-sploit.git
cd fouad-sploit
```

### 2. Create Branch

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or bug fix branch
git checkout -b fix/bug-description
```

### 3. Make Changes

```bash
# Edit files
vim fouad_sploit.py

# Test your changes
./fouad_sploit.py --help
```

### 4. Test Thoroughly

```bash
# Test different modes
./fouad_sploit.py --interactive
./fouad_sploit.py --auto --target 127.0.0.1
./fouad_sploit.py -t 127.0.0.1 -s

# Test with Python directly
python3 fouad_sploit.py --help
```

## 📤 Submitting Changes

### 1. Commit Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add: New exploit module for XYZ service"

# Use conventional commits:
# - feat: New feature
# - fix: Bug fix
# - docs: Documentation
# - style: Formatting
# - refactor: Code restructuring
# - test: Testing
# - chore: Maintenance
```

### 2. Push to Fork

```bash
# Push to your fork
git push origin feature/your-feature-name
```

### 3. Create Pull Request

1. Go to original repository
2. Click "New Pull Request"
3. Select your branch
4. Fill in:
   - Title: Clear and descriptive
   - Description: What changed and why
   - Related issues: Reference any issues
   - Testing: How you tested

### 4. Code Review

- Respond to feedback
- Make requested changes
- Keep discussion professional

## 📏 Style Guidelines

### Python Code Style

```python
# Follow PEP 8
# Use 4 spaces for indentation
# Maximum line length: 100 characters

# Good function naming
def detect_open_ports(host, port_range=None):
    """Scan for open ports on target"""
    pass

# Good variable naming
target_host = "192.168.1.100"
open_ports = []

# Use type hints where helpful
def scan_port(host: str, port: int, timeout: int = 1) -> bool:
    """Check if a port is open"""
    pass

# Document functions
def print_status(message: str, status: str = 'info'):
    """
    Print formatted status messages
    
    Args:
        message: Message to display
        status: Message type (info, success, error, warning, exploit)
    """
    pass
```

### Documentation Style

```markdown
# Use clear headings

## Section Title

### Subsection

- Use bullet points for lists
- **Bold** important terms
- `Code` in backticks
- ```code blocks``` for examples

# Include examples
# Explain why, not just what
```

### Commit Messages

```bash
# Good commit messages:
git commit -m "feat: Add BlueKeep RDP exploit module"
git commit -m "fix: Correct port scanning timeout issue"
git commit -m "docs: Update installation instructions for Ubuntu"
git commit -m "refactor: Improve error handling in auto_mode()"

# Bad commit messages:
git commit -m "update"
git commit -m "fix bug"
git commit -m "changes"
```

## 🧪 Testing Guidelines

### Manual Testing

```bash
# Test all modes
./fouad_sploit.py --auto --target 127.0.0.1
./fouad_sploit.py --interactive
./fouad_sploit.py -t 127.0.0.1 -s
./fouad_sploit.py -t 127.0.0.1 -p 445

# Test error handling
./fouad_sploit.py --target invalid_ip
./fouad_sploit.py --port 99999
```

### Security Testing

- Test with safe, authorized targets only
- Verify no hardcoded credentials
- Check for information leakage
- Ensure proper error handling

## 🎨 Adding Features

### New Exploit Module

```python
# In get_exploit_modules() function
'service_name': [
    'exploit/category/exploit_name',
],
```

### New Service Detection

```python
# In get_service_name() function
services = {
    port_number: 'Service Name',
}
```

### New Command Line Option

```python
# In main() function
parser.add_argument(
    '-x', '--your-option',
    help='Description of your option'
)
```

## 🐛 Bug Fix Process

1. Identify the bug
2. Create failing test case
3. Fix the bug
4. Verify fix works
5. Ensure no regression
6. Submit PR with test

## 📝 Documentation Updates

When updating code, also update:

- README.md
- CODE_EXAMPLES.md
- INSTALL.md
- Inline comments
- Function docstrings

## 💡 Feature Ideas

Want to contribute but not sure what? Try:

- Add new exploit modules
- Improve port scanning speed
- Add more service detection
- Create GUI version
- Add payload options
- Improve error messages
- Add logging features
- Create API wrapper
- Add multi-threading
- Improve banner design

## ✅ Pull Request Checklist

Before submitting:

- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tested on Kali Linux
- [ ] No security issues introduced
- [ ] Commit messages are clear
- [ ] Branch is up to date
- [ ] No merge conflicts
- [ ] Related issues referenced

## 📞 Contact

Questions about contributing?

📧 **Email:** zalaffouad37@gmail.com  
📱 **Instagram:** [@1.pvl](https://instagram.com/1.pvl)

## 🙏 Thank You!

Your contributions make **Fouad Sploit** better for everyone!

---

**Made with ❤️ by Fouad | © 2025**
