
# WhatsApp Chat Data Extractor

**Turn raw WhatsApp chats into structured data for AI and Machine Learning.**  
Refine the noise. Extract the oil. Build models that think.

## Overview

This Python tool transforms exported WhatsApp `.txt` files into clean, structured `.csv` datasets — the fuel for data-driven intelligence.

Extracted variables:
- `timestamp`: When the message was sent
- `sender`: Who sent the message
- `message`: The content (text/media)
- `media_flag`: Boolean indicator for media files

## Why This Matters

In the data economy, **conversations are oil.**  
WhatsApp groups contain:
- Behavioral signals  
- Social influence patterns  
- Language dynamics  
- Communication timing  
- Sentiment trails

**This script is your first pipeline** — converting unstructured chat into structured intelligence for analysis or model training.

## AI/ML Potential Use Cases

- NLP: Chatbot training, topic modeling, entity extraction
- Behavioral analysis: Active hours, dominant voices, engagement frequency
- Social graph generation: Interaction mapping & influence scoring
- Sentiment mining: Mood shifts and community health over time
- Predictive analytics: Conversation triggers, churn, disputes

## Features

- Regex-powered parsing engine
- Detects and flags media attachments
- Outputs structured `.csv` file
- Ready for Pandas, NumPy, and ML pipelines
- Lightweight, pure Python (no external libs)

data output is in CSV easy for R, python analysis 


Just don’t waste the oil😂

let's contribute 🤝😌


## Installation
```bash
git clone https://github.com/Neewtonium/whatsApDataRipper.git
cd whatsAppDataRipper
python whatsAppDataRipper.py

Input Format (Raw Export)

Example from WhatsApp:

29/04/2025, 09:42 - John Doe: Hello world
29/04/2025, 09:43 - Jane: <Media omitted>

Output Format (CSV)


