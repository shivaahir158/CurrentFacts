def store_context(claim, response):
    conversation_memory[claim] = response

def get_past_context():
    return conversation_memory