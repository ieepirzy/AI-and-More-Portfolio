from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)

# Simple text invocation
result = llm.invoke("Sing a ballad of LangChain.")
print(result.content)