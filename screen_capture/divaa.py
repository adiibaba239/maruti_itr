import time

import google.generativeai as genai


from specific_area import monitor_chat_area
# Initialize Pinecone client
genai.configure(api_key='')

# Configuration for the generative model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-pro",
    safety_settings=safety_settings
)

# Memory to store previous interactions
memory = []

#chat=capture_and_analyze_screen()
def handle_chat():
    global memory

    def format_memory(memory):
        formatted_memory = ""
        for interaction in memory:
            formatted_memory += f"User: {interaction['query']}\nAssistant: {interaction['response']}\n"
        print(formatted_memory)
        return formatted_memory

    def generate_response(query):
        context = format_memory(memory)
       # chat = capture_and_analyze_screen()
        prompt = (
            f"act like a chat bot whose name is diva made by aditya ,recognize the chat context and the chatting pattern from the text "
            f"and prepare a message for the recent message this is the chat content {query} and this is the context of you previous responses{context}"
            f"just give point to point response to message of user in the way he is talking"



        )

        result = model.generate_content(contents=prompt)
        response = result.text
        memory.append({"query": query, "response": response})
        print (response)
        print(query)
        return response



    while True:
        time.sleep(5)
        query = monitor_chat_area()

        if query is None:
            print("Could not understand audio. Please try again.")
            continue

        if "exit" in query:
            print("Exiting chat...")
            break

        response = generate_response(query)
        #speak2(response)


# Call handle_chat function to start
handle_chat()
