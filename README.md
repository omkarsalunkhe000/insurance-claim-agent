# Insurance Claim Agent

**AI-Powered Insurance Claims Processing System** using **LangGraph** multi-agent architecture.

## ✨ Features

- ✅ Automated Claim Validation
- 🔍 Fraud Detection
- 📋 Policy Compliance Checking
- 📄 Multi-format Document Analysis (PDF, Images)
- 🤖 Intelligent Decision Making
- 👤 Human-in-the-Loop Escalation
- 📊 Detailed Audit & Reporting

## 🛠 Tech Stack

- **LangGraph** + **LangChain**
- Grok / OpenAI / Anthropic LLMs
- Streamlit (Frontend)
- FAISS Vector Store
- Pydantic for state management

## 🚀 Quick Start

```bash
git clone https://github.com/omkarsalunkhe000/insurance-claim-agent.git
cd insurance-claim-agent
pip install -r requirements.txt
cp .env.example .env
# Add your API keys in .env
streamlit run main.py
```

## Project Structure

```bash
insurance-claim-agent/
├── agent/           # LangGraph nodes & graph
├── prompts/         # System & agent prompts
├── tools/           # Custom tools
├── data/            # Sample claims & policies
├── main.py          # UI entry point
├── requirements.txt
└── README.md
```

## Next Steps

Reply with what you want next:
- Complete agent code
- Streamlit UI
- Sample policies & claims
- Fraud detection logic

Built with ❤️ using Grok