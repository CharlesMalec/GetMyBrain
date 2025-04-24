# Knowledge-Gathering AI Tool

![Project Status](https://img.shields.io/badge/status-in%20progress-blue)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

An AI-powered tool to gather knowledge about business functions (e.g., "Manage a PPA") through a conversational large language model (LLM). The tool captures processes and operational activities, adapts to client feedback, accounts for local specificities (e.g., Germany, France, Netherlands), and generates a structured Markdown wiki.

## 🚀 Project Overview

The Knowledge-Gathering AI Tool enables users to document business functions via a dynamic Q&A interface. Starting with the question, "Which function shall we start with?", it builds a knowledge base by adapting questions based on user responses and incorporating local regulations. The output is a clean, structured Markdown wiki, ideal for process documentation and knowledge sharing.

- **Backend**: Python (Flask), SQLite
- **Frontend**: React (planned for Phase 2)
- **LLM**: xAI Grok API or Hugging Face LLaMA
- **Repository**: [github.com/CharlesMalec/GetMyBrain](https://github.com/CharlesMalec/GetMyBrain)
- **Trello Board**: [trello.com/b/eWZc9Ja4/knowledge-gathering-tool](https://trello.com/b/eWZc9Ja4/knowledge-gathering-tool)

## 📋 Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/CharlesMalec/GetMyBrain.git
   cd GetMyBrain