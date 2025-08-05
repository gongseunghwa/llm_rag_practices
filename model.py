from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
# from langchain import ChatBedrock

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

### chat model
llm_model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature=0,
)

embed_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")