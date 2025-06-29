def format_response(claim, match_result, sources):
    return {
        "claim": claim,
        "verdict": match_result,
        "sources": list(sources.keys()),
        "notes": f"Sources analyzed: {len(sources)}"
    }