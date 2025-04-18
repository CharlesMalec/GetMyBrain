Knowledge-Gathering AI Tool

An AI-powered tool to gather knowledge about business functions (e.g., "Manage a PPA") through a conversational LLM. It captures processes and operational activities, adapts to client feedback, accounts for local specificities (e.g., Germany, France), and generates a structured Markdown wiki.

Setup

Backend: Python (Flask), SQLite
Frontend: React (planned)
LLM: xAI Grok API or Hugging Face LLaMA
Install: pip install -r backend/requirements.txt
Run: python backend/app.py

Trello Board

https://trello.com/b/eWZc9Ja4/knowledge-gathering-tool

Artifacts

Requirements: docs/requirements.md
Backend: backend/app.py
Dependencies: backend/requirements.txt
Trello Structure: docs/trello_board.json
Trello Setup Script: scripts/create_trello_board.py
