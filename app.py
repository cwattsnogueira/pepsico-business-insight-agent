import os
import gradio as gr
from agent.orchestrator import run_agent

# Predefined high‑impact business questions
PRESET_QUESTIONS = [
    "Analyze Gatorade’s performance last quarter and identify key drivers.",
    "What strategic opportunities should Gatorade prioritize next quarter?",
    "How should Gatorade respond to competition from Prime and BodyArmor?",
    "What hydration trends are shaping consumer behavior in 2025?",
    "What marketing actions would most effectively increase Gatorade’s Gen Z engagement?",
    "What supply chain risks could impact Gatorade’s performance in the next 6 months?",
    "If sports drink category growth slows by 3%, what actions should PepsiCo take?",
    "Summarize Gatorade’s strategic priorities for 2025 in 5 bullet points."
]

def load_question(selected):
    return selected  # fills the textbox with the selected question

def chat(user_input):
    return run_agent(user_input)

with gr.Blocks(title="PepsiCo AI Agent") as demo:
    gr.Markdown("### PepsiCo Business Insight Agent\nSelect a question or type your own.")

    with gr.Row():
        dropdown = gr.Dropdown(
            PRESET_QUESTIONS,
            label="Select a Business Question",
            interactive=True
        )

    user_box = gr.Textbox(
        label="Ask the Agent",
        placeholder="Type your question or select one above..."
    )

    dropdown.change(load_question, inputs=dropdown, outputs=user_box)

    output = gr.Textbox(label="Agent Response")

    submit_btn = gr.Button("Generate Insight")
    submit_btn.click(chat, inputs=user_box, outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)

