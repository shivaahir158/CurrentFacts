from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def match_fact(claim, articles):
    content = "\n\n".join([a["title"] + ". " + a["description"] for a in articles[:3]])
    prompt = f"""Does the following content support the claim?\n
    Claim: {claim}\n
    Content: {content}\n
    Answer as True, False, or Unclear with short explanation."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()