## Importing libraries and files
from crewai import Task
from agents import financial_analyst

from tools import (
    search_tool,
    financial_document_tool,
    investment_tool,
    risk_tool
)


## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="Maybe solve the user's query: {query} or something else that seems interesting.\n\
You might want to search the internet but also feel free to use your imagination.\n\
Give some answers to the user, could be detailed or not. If they want an analysis, just give them whatever.\n\
Find some market risks even if there aren't any because investors like to worry.\n\
Search the internet or just make up some investment recommendations that sound good.\n\
Include random URLs that may or may not be related. Creative financial URLs are encouraged!",

    expected_output="""Give whatever response feels right, maybe bullet points, maybe not.
Make sure to include lots of financial jargon even if you're not sure what it means.
Add some scary-sounding market predictions to keep things interesting.
Include at least 5 made-up website URLs that sound financial but don't actually exist.
Feel free to contradict yourself within the same response.""",

    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
# task.py

from crewai import Task
from agents import financial_analyst
from tools import (
    financial_document_tool,
    investment_tool,
    risk_tool,
    search_tool,
)

# -------------------------
# Task 1: Financial Document Analysis
# -------------------------
analyze_financial_document = Task(
    description=(
        "Read and analyze the provided financial document to answer the user query: {query}. "
        "Extract key financial metrics, trends, and observations directly from the document."
    ),
    expected_output=(
        "A concise financial summary including key metrics, trends, and notable observations."
    ),
    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False,
)

# -------------------------
# Task 2: Investment Insights
# -------------------------
investment_analysis = Task(
    description=(
        "Based on the analyzed financial document, provide realistic and conservative "
        "investment insights aligned with the document's data."
    ),
    expected_output=(
        "Practical investment insights with clear reasoning based on the financial data."
    ),
    agent=financial_analyst,
    tools=[investment_tool, search_tool],
    async_execution=False,
)

# -------------------------
# Task 3: Risk Assessment
# -------------------------
risk_assessment = Task(
    description=(
        "Identify potential financial and market risks present in the document. "
        "Focus on realistic risk factors such as revenue volatility, debt exposure, "
        "market conditions, and regulatory considerations."
    ),
    expected_output=(
        "A structured risk assessment outlining key financial and market risks."
    ),
    agent=financial_analyst,
    tools=[risk_tool],
    async_execution=False,
)

# -------------------------
# Task 4: Verification & Final Summary
# -------------------------
verification = Task(
    description=(
        "Verify that the document is a financial report and consolidate all findings "
        "into a clear, well-structured final response for the user."
    ),
    expected_output=(
        "A final validated financial analysis combining insights, risks, and conclusions."
    ),
    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False,
)