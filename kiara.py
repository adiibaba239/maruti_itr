import google.generativeai as genai
from speech_handler import speak, listen
from speak_function import speak as speak2

# Initialize Pinecone client
genai.configure(api_key='AIzaSyCay112ajwakcbG6l5wTLK5WTSKBlzJH44')

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


def handle_chat():
    global memory

    def format_memory(memory):
        formatted_memory = ""
        for interaction in memory:
            formatted_memory += f"User: {interaction['query']}\nAssistant: {interaction['response']}\n"
        #print(formatted_memory)
        return formatted_memory

    def generate_response(query):
        context = format_memory(memory)
        prompt = (
            f" "
            f"choose the one diagram from the following that is more suitable: "
            f"""
                            1. **Flowchart** - A diagram using `graph TD` or `graph LR`.
                            2. **Sequence Diagram** - A diagram using `sequenceDiagram`.
                            3. **Class Diagram** - A diagram using `classDiagram`.
                            4. **State Diagram** - A diagram using `stateDiagram`.
                            5. **Gantt Chart** - A chart using `gantt`.
                            6. **Entity-Relationship Diagram (ERD)** - A diagram using `erDiagram`.
                            7. **Pie Chart** - A chart using `pie`.
                            8. **User Journey Diagram** - A diagram using `journey`.
                            9. **Git Graph** - A graph using `gitGraph`.
                            10. **Mind Map** - A diagram using `mindmap`.
        )""")

        result = model.generate_content(contents=prompt)
        response = result.text
        memory.append({"query": query, "response": response})
        print (response)
        return response



    while True:
        query = (""""""
""" )

        if query is None:
            print("Could not understand audio. Please try again.")
            continue

        if "exit" in query:
            print("Exiting chat...")
            break

        response = generate_response(query)
        print(response)
        #speak2(response)


# Call handle_chat function to start
handle_chat()
