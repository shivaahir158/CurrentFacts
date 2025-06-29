# CurrentFacts – AI-Powered Fact Checker for Current Events

CurrentFacts is a Python-based backend system that checks the credibility of real-world claims using multiple agents. It parses natural language queries, searches news sources, and evaluates the factual accuracy using LLMs and APIs. Think of it as a lightweight fact-checking engine with plug-and-play agent logic.

---

## What It Does

- Takes in a user-submitted claim (e.g. "India signed an FTA with the EU")
- Breaks it down to identify the core topic
- Searches recent news articles using NewsAPI
- Uses OpenAI to compare the claim with what’s in the news
- Responds with a verdict: True / False / Unclear
- Returns supporting sources + notes

---

## Tech Stack

| Layer        | Tech                           |
|--------------|--------------------------------|
| LLM          | OpenAI GPT (via API)           |
| API Layer    | FastAPI                        |
| Search       | NewsAPI                        |
| Orchestration| Custom agent logic (Python)    |
| Memory       | Simulated MCP via Python dict  |
| Testing UI   | Swagger (via FastAPI)          |

---

## How to Run

1. Clone the repo

```bash
git clone https://github.com/your-username/currentfacts.git
cd currentfacts
