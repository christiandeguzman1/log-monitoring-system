<p align="center">
  <img src="https://img.shields.io/badge/Python-Project-blue" />
  <img src="https://img.shields.io/badge/DevOps-Automation-green" />
  <img src="https://img.shields.io/badge/Monitoring-System-orange" />
</p>

## Automated Log Monitoring & Incident Alert System

A real-time log monitoring system built with Python and watchdog that detects anomalies and stores incidents in SQLite.

## Features
- Real-time log file monitoring
- Regex-based anomaly detection
- Incident storage in SQLite database
- Console-based alert system
- Thread-safe database handling

## Tech Stack
- Python
- SQLite
- watchdog
- Regex

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
