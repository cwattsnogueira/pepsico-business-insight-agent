import os
from dotenv import load_dotenv

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.memory import ConversationBufferMemory
from langchain.prompts import SystemMessagePromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.4,
    api_key=os.getenv("OPENAI_API_KEY")
)

# SYSTEM PROMPT (Your Agent Brain)

SYSTEM_PROMPT = """
You are a Senior Business Insight Agent specializing in enterprise strategy, consumer behavior,
supply chain, marketing effectiveness, and brand performance.

Your role is to support executive decision‑making at PepsiCo by generating clear, structured,
insight‑driven analysis.

Your responsibilities:
- Interpret any business question and identify the relevant domain (brand performance, supply chain,
  marketing, finance, consumer trends).
- Even without real-time data, provide insights using historical patterns, category dynamics,
  competitive context, and strategic reasoning.
- Never say “I don’t have access to real-time data.” Instead, acknowledge the limitation briefly and
  deliver a high‑value analysis.
- Always communicate in an executive-friendly tone: concise, confident, and actionable.

For every business question, output:

1. Key Insight
2. Business Impact
3. Recommended Actions
4. Risks & Considerations

Guidelines:
- Be specific, analytical, and business-oriented.
- Use industry logic, not generic statements.
- When discussing brands (e.g., Gatorade, Pepsi, Lay’s), incorporate performance drivers,
  competitive landscape, and consumer behavior.
- When discussing supply chain, consider logistics, cost pressures, resilience, and efficiency.
- When discussing marketing, consider segmentation, channels, messaging, and ROI.
- When discussing consumer behavior, consider demographics, motivations, and emerging trends.

Your goal is to deliver insights that feel like they came from a seasoned PepsiCo strategist.
"""

system_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT)


# TOOLS (Agent Capabilities)

search_tool = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="web_search",
        func=search_tool.run,
        description="Useful for searching the web for recent information, trends, competitors, or market signals."
    )
]


# MEMORY (Agent Short-Term Memory)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)


# BUILD THE AGENT

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,   # structured for reasoning + tool use
    verbose=True,
    memory=memory,
    system_message=system_prompt
)


# RUN AGENT FUNCTION

def run_agent(user_input: str) -> str:
    """Run the LangChain agent with memory + tools."""
    response = agent.run(user_input)
    return response
