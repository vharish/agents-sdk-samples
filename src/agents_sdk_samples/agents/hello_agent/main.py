import os

from agents import Runner
from dotenv import load_dotenv

from ...common.exceptions import ApiKeyNotFoundError
from .agent import agent

# Load environment variables from .env.local
load_dotenv(dotenv_path=".env.local")

# Get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ApiKeyNotFoundError()

# The openai-agents SDK automatically uses the OPENAI_API_KEY environment variable.
# No need to pass it explicitly to the client.

# Create a runner
output = Runner.run_sync(agent, input="Write a haiku about recursion in programming.")

# Print the final output
print(output.final_output)
