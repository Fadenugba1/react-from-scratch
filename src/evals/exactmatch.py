from vertexai.generative_models import HarmBlockThreshold
from vertexai.generative_models import GenerationConfig
from vertexai.generative_models import GenerativeModel
from vertexai.generative_models import HarmCategory
from vertexai.generative_models import Part
from google import genai
from google.genai.types import HttpOptions
from src.config.logging import logger
from typing import Optional
from typing import Dict
from typing import List 
from src.llm.gemini import *
from src.react.agent import run
from src.config.logging import setup_logger





def exact_match(client,questions:List[str])->None:
    for q in questions:
        
        model_response = client.models.generate_content(model="gemini-2.5-flash",contents=q,)
        #generates response from gemini 2.0 model
        agent_response = run(q)
        print(model_response.text)
        print(agent_response)

if __name__ == "__main__":
    logger = setup_logger()
    #Questions generated from "ReAct: Synergizing Reasoning and Acting in Language Models" paper
    questions = ["Aside from the apple remote, what other apple device can control the program the apple remote was initially designed to interact with?","How many rooms are there in the hotel that is home to the Cirque du Soleil show Mystere?"]
    client = genai.Client(vertexai=True,
    project="plexiform-bot-382022",
    location="us-central1")
    exact_match(client,questions)
