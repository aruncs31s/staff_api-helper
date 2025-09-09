# Staff API Helper

A Python-based helper application for managing staff data that interacts with the [etlab_backend_go_staff_module](https://github.com/aruncs31s/etlab_backend_go_staff_module) Go backend API.

## Features

- 📝 Register new staff members from predefined data
- 📋 Retrieve and display all registered staff
- 🎓 Create and manage staff qualifications
- 🖥️ Interactive menu-driven console interface

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure the Go backend API is running on `localhost:9090`

3. Run the application:
   ```bash
   cd src
   python app.py
   ```

## Project Structure

- `src/app.py` - Main application with menu interface
- `src/apis/api.py` - HTTP API client for backend communication
- `src/files/files.py` - JSON file handler for staff data
- `src/formater/staff_info.py` - Data formatting utilities
- `data/new_staff_details.json` - Sample staff data

## API Integration

This helper tool communicates with a Go backend API that uses:
- **Framework**: Gin (HTTP web framework)
- **ORM**: GORM (Object-Relational Mapping)
- **Endpoints**: RESTful staff management API

## Contributing

See `.github/copilot-instructions.md` for detailed project context and development guidelines.