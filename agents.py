from crewai import Agent
from tools import search_tool, financial_document_tool

financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze financial documents and provide insights",
    backstory="An experienced financial analyst skilled in investment analysis and risk assessment.",
    tools=[search_tool, financial_document_tool],
    verbose=True,
)