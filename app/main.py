from fastapi import FastAPI
from pydantic import BaseModel
from agents.claim_parser import parse_claim
from agents.search_agent import search_news
from agents.fact_matcher import match_fact
from agents.sentiment_analyzer import analyze_sentiment
from agents.response_agent import format_response
from mcp.context_manager import store_context

app = FastAPI()

class ClaimRequest(BaseModel):
    claim: str

@app.post("/verify")
def verify_claim(request: ClaimRequest):
    claim = request.claim
    parsed = parse_claim(claim)
    articles = search_news(claim)
    verdict = match_fact(claim, articles)
    sentiments = analyze_sentiment(articles)
    response = format_response(claim, verdict, sentiments)
    store_context(claim, response)
    return response