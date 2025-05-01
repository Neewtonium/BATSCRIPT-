
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

## Installation

```bash
git clone https://github.com/Neewtonium/whatsapp-data-extractor.git
cd whatsapp-data-extractor
python whatsapp_parser.py

Input Format (Raw Export)

Example from WhatsApp:

29/04/2025, 09:42 - John Doe: Hello world
29/04/2025, 09:43 - Jane: <Media omitted>

Output Format (CSV)

Roadmap

[ ] Auto sentiment detection

[ ] Word frequency / NLP vectorization

[ ] Message length & engagement scoring

[ ] Graph-based relationship mapping

[ ] Web-based dashboard for real-time analysis


License

MIT License — use it, abuse it, evolve it.
Just don’t waste the oil.

About

Built by Newton Ojwang
Student. Architect of Lab of Eden. Refiner of digital chaos.
Data is oil. AI is the engine. This is the refinery.


---

> “Silently, you build. Ruthlessly, you extract. Unmercifully, you refine.”
— Lab of Eden Philosophy



---

You want me to generate the repo structure and push steps as well?

