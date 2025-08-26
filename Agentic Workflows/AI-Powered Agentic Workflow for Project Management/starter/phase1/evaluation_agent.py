# TODO: 1 - Import EvaluationAgent and KnowledgeAugmentedPromptAgent classes
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, EvaluationAgent
import os
from dotenv import load_dotenv, find_dotenv

# Load nearest .env and OVERRIDE existing vars
load_dotenv(find_dotenv(usecwd=True), override=True)

api_key = os.getenv("OPENAI_API_KEY")
assert api_key, "OPENAI_API_KEY not loaded from .env"

openai_api_key = os.getenv("OPENAI_API_KEY")
prompt = "What is the capital of France?"

# Parameters for the Knowledge Agent
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capitol of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge) # TODO: 2 - Instantiate the KnowledgeAugmentedPromptAgent here

# Parameters for the Evaluation Agent
persona = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a sentence."
evaluation_agent = EvaluationAgent(openai_api_key, persona, evaluation_criteria, knowledge_agent, 10) # TODO: 3 - Instantiate the EvaluationAgent with a maximum of 10 interactions here

# TODO: 4 - Evaluate the prompt and print the response from the EvaluationAgent
evaluation_agent_response = evaluation_agent.evaluate(prompt)

print(evaluation_agent_response)
