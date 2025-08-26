# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv, find_dotenv

# Load nearest .env and OVERRIDE existing vars
load_dotenv(find_dotenv(usecwd=True), override=True)

api_key = os.getenv("OPENAI_API_KEY")
assert api_key, "OPENAI_API_KEY not loaded from .env"

openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris."
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
knowledge_augmented_agent_response = KnowledgeAugmentedPromptAgent(api_key, persona, knowledge).respond(prompt)

# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
print(knowledge_augmented_agent_response)
print("The agent used provided knowledge to respond to the user query instead of its own inherent knowledge.")