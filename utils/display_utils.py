from groq import Groq

groq_client = Groq(api_key="enter your api key")

def generate_response(query, relevant_text, relevant_images):
    context = "\n".join(relevant_text)
    prompt = f"""Context: {context}
    Query: {query}
    if the infomation is not present in the text, generate a response "Sorry. The information is not available" and give a short summary on the revelant texts .
    """
    response = groq_client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides information based on the given context."},
            {"role": "user", "content": prompt}
        ],
        model="llama3-70b-8192", 
        max_tokens=1000
    )
    return response.choices[0].message.content

def display_results(response, relevant_text, relevant_images):
    print("\n--- Generated Response ---")
    print(response)
    print("\n--- Relevant Text Excerpts ---")
    for i, text in enumerate(relevant_text, 1):
        print(f"{i}. {text[:100]}...")
    print("\n--- Relevant Image IDs ---")
    print(relevant_images)
