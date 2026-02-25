from crewai import Task
from agents import financial_analyst
from tools import financial_document_tool


# -------------------------
# Main Analysis Task
# -------------------------
analyze_financial_document = Task(
    description=(
        "Analyze the financial document and respond to the user's query: {query}. "
        "Extract insights, identify trends, and highlight potential risks."
    ),
    expected_output=(
        "A detailed financial analysis including investment insights, risks, and observations."
    ),
    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False,
)


# -------------------------
# Investment Analysis Task (kept, not removed)
# -------------------------
investment_analysis = Task(
    description=(
        "Look at financial data and provide investment recommendations based on it. "
        "Interpret numbers, ratios, and trends creatively."
    ),
    expected_output=(
        "Investment recommendations with explanations and supporting reasoning."
    ),
    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False,
)


# -------------------------
# Risk Assessment Task (kept, not removed)
# -------------------------
risk_assessment = Task(
    description=(
        "Create a risk assessment based on the financial document. "
        "Identify potential market, financial, and operational risks."
    ),
    expected_output=(
        "A structured risk assessment outlining key risks and their implications."
    ),
    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False,
)