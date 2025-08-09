# ================================================================
# agent_executor.py - Multi-Skill Agent Executor
# ================================================================
# PURPOSE: Contains the core logic for handling multiple skills in a single executor
#
# COMPONENTS:
# - GreetingAgent: Returns friendly greetings
# - QuoteAgent: Returns motivational quotes
# - MultiSkillAgentExecutor: Routes messages based on keywords
#
# ROUTING LOGIC:
# - Greeting keywords: "hello", "hi", "hey", "greet", "greeting"
# - Quote keywords: "quote", "inspire", "motivate", "motivation", "inspiration"
# - Default: Falls back to greeting for unrecognized messages
#
# ARCHITECTURE: Single executor pattern with keyword-based message routing
# ================================================================
from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.utils import new_agent_text_message
from pydantic import BaseModel


class GreetingAgent(BaseModel):
    """Greeting agent that returns a greeting"""

    async def invoke(self) -> str:
        return "Hello! I'm your friendly greeting agent. Nice to meet you!"


class QuoteAgent(BaseModel):
    """Quote agent that returns motivational quotes"""

    async def invoke(self) -> str:
        return "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine!"


class MultiSkillAgentExecutor(AgentExecutor):
    """Single executor that handles both greeting and quote skills"""

    def __init__(self):
        self.greeting_agent = GreetingAgent()
        self.quote_agent = QuoteAgent()

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        # Get the message text to determine which skill to use
        message_text = ""
        if hasattr(context, 'message') and context.message and context.message.parts:
            for part in context.message.parts:
                if hasattr(part, 'text'):
                    message_text += part.text
                elif hasattr(part, 'root') and hasattr(part.root, 'text'):
                    message_text += part.root.text
        
        message_text = message_text.lower().strip()
        print(f"DEBUG: Received message: '{message_text}'")
        
        # Simple keyword-based routing
        quote_keywords = ["quote", "inspire", "motivate", "motivation", "inspiration"]
        greeting_keywords = ["hello", "hi", "hey", "greet", "greeting"]
        
        result = None
        
        # Check for quote keywords
        if any(keyword in message_text for keyword in quote_keywords):
            print("DEBUG: Routing to quote agent")
            result = await self.quote_agent.invoke()
        
        # Check for greeting keywords or default to greeting
        elif any(keyword in message_text for keyword in greeting_keywords) or not message_text:
            print("DEBUG: Routing to greeting agent")
            result = await self.greeting_agent.invoke()
        
        # Default fallback
        else:
            print("DEBUG: No specific keywords found, defaulting to greeting")
            result = await self.greeting_agent.invoke()
        
        event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        raise Exception("Cancel not supported")