import os 
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

class Configloader:
    def __init__(self):
        print(f"Loaded config....")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider: Literal["groq", "openai"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __contex: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitary_types_allowed = True

    def load_llm(self):
        """
        Load and return  the LLM model.
        
        """
        print("LLM loading .....")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading LLM from groq ......")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model = model_name, api_key = groq_api_key)
        elif self.model_provider == "openai":
            print("Loading LLM from openai .....")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model = model_name, api_key = openai_api_key)
        
        return llm