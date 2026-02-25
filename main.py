from database import engine
from models import AnalysisResult
from database import Base
from database import SessionLocal
from models import AnalysisResult
from dotenv import load_dotenv
load_dotenv()


Base.metadata.create_all(bind=engine)
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, file_path: str):
    import os
    from database import SessionLocal
    from models import AnalysisResult

    result = None

    try:
        # Try normal CrewAI execution
        if os.getenv("OPENAI_API_KEY"):
            financial_crew = Crew(
                agents=[financial_analyst],
                tasks=[analyze_financial_document],
                process=Process.sequential,
            )

            result = financial_crew.kickoff(
                {"query": query, "file_path": file_path}
            )
        else:
            raise RuntimeError("No OPENAI_API_KEY set")

    except Exception as crew_error:
        # Graceful fallback (NO LLM dependency)
        result = {
            "summary": "LLM execution skipped or failed. Returned fallback analysis.",
            "investment_recommendations": [
                "Diversify investments across sectors.",
                "Focus on long-term fundamentals.",
                "Avoid excessive exposure to high-risk assets."
            ],
            "risk_assessment": [
                "Market volatility risk",
                "Economic uncertainty",
                "Liquidity constraints"
            ],
            "market_insights": [
                "Markets remain sensitive to macroeconomic signals.",
                "Long-term growth outlook appears stable.",
                "Short-term fluctuations are expected."
            ],
            "debug_note": str(crew_error)
        }

    # Persist result to database
    db = SessionLocal()
    try:
        record = AnalysisResult(
            filename=file_path,
            query=query,
            result=str(result),
        )
        db.add(record)
        db.commit()
    except Exception as e:
        print("DB write failed:", e)
    finally:
        db.close()

    return result

@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights"),
):
    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())

        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
@app.get("/history")
def get_history():
    db = SessionLocal()
    records = db.query(AnalysisResult).all()
    db.close()

    return [
        {
            "id": r.id,
            "filename": r.filename,
            "query": r.query,
            "created_at": r.created_at,
        }
        for r in records
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)