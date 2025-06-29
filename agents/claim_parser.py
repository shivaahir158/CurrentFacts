from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def parse_claim(claim):
    prompt = f"""Extract key entities (who, what, when) from this claim:
    \nClaim: {claim}\n"""
    response = client.chat.completions.create(
        #model="gpt-4"
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )