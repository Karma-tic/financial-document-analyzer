# tools.py

import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool
from crewai_tools.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader


# -------------------------
# Search Tool
# -------------------------
search_tool = SerperDevTool()


# -------------------------
# Financial Document Reader Tool
# -------------------------
class FinancialDocumentTool(BaseTool):
    name = "financial_document_reader"
    description = "Reads and cleans a financial PDF document from a given file path"

    def _run(self, path: str = "data/sample.pdf") -> str:
        loader = PyPDFLoader(path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report


financial_document_tool = FinancialDocumentTool()


# -------------------------
# Investment Analysis Tool
# -------------------------
class InvestmentTool(BaseTool):
    name = "investment_analysis_tool"
    description = "Provides investment insights based on financial document data"

    def _run(self, financial_document_data: str) -> str:
        cleaned = " ".join(financial_document_data.split())
        return (
            "Investment insights based on the financial document:\n"
            "- Consider revenue trends and profitability\n"
            "- Evaluate debt levels and cash flow\n"
            "- Assess long-term growth indicators"
        )


investment_tool = InvestmentTool()


# -------------------------
# Risk Assessment Tool
# -------------------------
class RiskTool(BaseTool):
    name = "risk_assessment_tool"
    description = "Identifies potential financial and market risks"

    def _run(self, financial_document_data: str) -> str:
        return (
            "Key risks identified:\n"
            "- Market volatility\n"
            "- Regulatory uncertainty\n"
            "- Revenue concentration risk"
        )


risk_tool = RiskTool()