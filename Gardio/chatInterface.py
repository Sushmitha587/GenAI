import gradio as gr

# Dummy function for generating AI responses
# Replace this with your LLM inference function (e.g., OpenAI API, HuggingFace pipeline, etc.)
def chatbot(message, chat_history):
    response = f"AI: You said '{message}'"  # Replace this with your LLM model output
    chat_history = chat_history or []
    chat_history.append((message, response))
    return chat_history, chat_history

# Gradio Chat Interface
with gr.Blocks() as demo:
    gr.Markdown("## Chat with your LLM")
    
    chatbot_ui = gr.Chatbot()           # Chat-style UI
    msg = gr.Textbox(label="Enter message")
    clear = gr.Button("Clear Chat")
    
    # Send message
    msg.submit(chatbot, [msg, chatbot_ui], [chatbot_ui, chatbot_ui])
    clear.click(lambda: [], None, chatbot_ui)

demo.launch()
