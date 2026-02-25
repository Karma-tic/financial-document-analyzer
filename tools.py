import os
from dotenv import load_dotenv

load_dotenv()

from crewai_tools import SerperDevTool
from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader


# -------------------------
# Search Tool (unchanged)
# -------------------------
search_tool = SerperDevTool()


# -------------------------
# Financial Document Tool
# Proper CrewAI BaseTool subclass
# -------------------------
class FinancialDocumentTool(BaseTool):
    name: str = "financial_document_tool"
    description: str = "Reads and cleans a financial PDF document from a given path."

    def _run(self, path: str = "data/sample.pdf") -> str:
        loader = PyPDFLoader(path)
        docs = loader.load()

        full_report = ""
        for doc in docs:
            content = doc.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report


# instantiate tool object
financial_document_tool = FinancialDocumentTool()