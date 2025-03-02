from app.integrations.gemini_api import generate_chatbot_reply

def get_chatbot_response(query: str) -> str:
    """
    Processes the user query with optional document summary context and returns a chatbot response.

    Args:
        query (str): The user's input query.
        document_summary (str, optional): Context extracted from a document to improve response quality.

    Returns:
        str: The chatbot's response.
    """
    try:
        #The query
        prompt = f"User Query: {query}"
        
        # Call the Gemini API to get a response
        response = generate_chatbot_reply(prompt)
        return response
    except Exception as e:
        return f"Error generating chatbot response: {str(e)}"
