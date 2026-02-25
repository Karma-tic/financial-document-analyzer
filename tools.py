# Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader

# Creating search tool
search_tool = SerperDevTool()

# Creating custom pdf reader tool
class FinancialDocumentTool:
    @staticmethod
    async def read_data_tool(path: str = "data/sample.pdf"):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file
        """
        loader = PyPDFLoader(path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            content = data.page_content

            # Clean and format the financial document data
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report


# Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    async def analyze_investment_tool(financial_document_data):
        processed_data = financial_document_data

        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        return "Investment analysis functionality to be implemented"


# Creating Risk Assessment Tool
class RiskTool:
    @staticmethod
    async def create_risk_assessment_tool(financial_document_data):
        return "Risk assessment functionality to be implemented"