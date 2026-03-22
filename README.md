# ML4DQM - GSoC 2026 Proposal

## Overview
This project focuses on improving Data Quality Monitoring (DQM) in high-energy physics using AI-based anomaly detection techniques.

## Problem
Current DQM systems rely heavily on manual monitoring, making them inefficient and prone to missing subtle anomalies in detector data.

## Proposed Solution
This project proposes an AI-driven pipeline that:
- Detects anomalies in real-time
- Assists human operators in decision-making
- Improves monitoring efficiency and accuracy

## Architecture
Detector → Preprocessing → Feature Extraction → ML Model → Alert System

## Tech Stack
- Python
- PyTorch
- TensorFlow
- FastAPI
- Docker

## Future Scope
- Real-time deployment
- Integration with CMS workflows
- Advanced deep learning models

## Author
Bhawna Mittal  
Bharati Vidyapeeth's College of Engineering, New Delhi
## 🚀 Demo Implementation

This repository includes a simple anomaly detection system (`demo.py`) that simulates real-time detector data and identifies anomalies using threshold-based detection.

### ▶️ How to run
```bash
python demo.py

### Visualization
The demo also includes a simple plot to visualize detected anomalies in the data stream.
