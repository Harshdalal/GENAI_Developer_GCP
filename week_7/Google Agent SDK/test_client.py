# ================================================================
# test_client.py - Interactive Test Client
# ================================================================
# PURPOSE: Provides user-friendly interface to test the multi-skill agent
#
# FEATURES:
# - Fetches agent card from server
# - Interactive menu with 5 options:
#   1. Test greeting skill with custom/default messages
#   2. Test quote skill with custom/default messages
#   3. Send completely custom messages
#   4. Run all predefined tests automatically
#   5. Exit application
#
# FUNCTIONALITY:
# - Connects to A2A server on localhost:9999
# - Sends messages and displays formatted responses
# - Extracts response text from A2A message format
# - Provides continuous testing loop with user choices
#
# USAGE: uv run --active test_client.py (after starting server)
# ================================================================
import uuid
import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import (
    AgentCard,
    Message,
    MessageSendParams,
    Part,
    Role,
    SendMessageRequest,
    TextPart,
)

PUBLIC_AGENT_CARD_PATH = "/.well-known/agent.json"
BASE_URL = "http://localhost:9999"


async def test_message(client: A2AClient, message_text: str, description: str):
    print(f"\n--- {description} ---")
    print(f"Sending: '{message_text}'")
    
    message_payload = Message(
        role=Role.user,
        messageId=str(uuid.uuid4()),
        parts=[Part(root=TextPart(text=message_text))],
    )
    request = SendMessageRequest(
        id=str(uuid.uuid4()),
        params=MessageSendParams(
            message=message_payload,
        ),
    )

    response = await client.send_message(request)
    
    # Extract response text from the JSON structure
    response_text = "No response text found"
    
    try:
        # Access the response as a dictionary using model_dump()
        response_dict = response.model_dump()
        
        if 'result' in response_dict and response_dict['result']:
            result = response_dict['result']
            if 'parts' in result and result['parts']:
                for part in result['parts']:
                    if 'text' in part and part['text']:
                        response_text = part['text']
                        break
                        
    except Exception as e:
        print(f"Error extracting response text: {e}")
    
    print(f"✅ Response: {response_text}")
    return response


async def main() -> None:
    async with httpx.AsyncClient() as httpx_client:
        # Initialize A2ACardResolver
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=BASE_URL,
        )

        try:
            print(f"Fetching agent card from: {BASE_URL}{PUBLIC_AGENT_CARD_PATH}")
            agent_card = await resolver.get_agent_card()
            print("✅ Fetched agent card successfully")
            print(f"Agent: {agent_card.name}")
            print(f"Skills: {[skill.name for skill in agent_card.skills]}")

        except Exception as e:
            print(f"❌ Error fetching agent card: {e}")
            raise RuntimeError("Failed to fetch agent card")

        client = A2AClient(
            httpx_client=httpx_client, agent_card=agent_card
        )
        print("✅ A2AClient initialized")

        # Interactive menu
        while True:
            print("\n" + "="*50)
            print("🤖 MULTI-SKILL AGENT TESTER")
            print("="*50)
            print("Choose what to test:")
            print("1. 🖐️  Greeting (hello, hi, hey)")
            print("2. 💪 Quote/Motivation (quote, inspire, motivate)")
            print("3. 🎲 Custom message")
            print("4. 🚀 Run all tests")
            print("5. ❌ Exit")
            print("-"*50)
            
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == "1":
                print("\n🖐️ Testing Greeting Skill...")
                message = input("Enter greeting message (or press Enter for 'Hello'): ").strip()
                if not message:
                    message = "Hello"
                await test_message(client, message, "Greeting Test")
                
            elif choice == "2":
                print("\n💪 Testing Quote/Motivation Skill...")
                message = input("Enter motivation request (or press Enter for 'Give me a quote'): ").strip()
                if not message:
                    message = "Give me a quote"
                await test_message(client, message, "Quote Test")
                
            elif choice == "3":
                print("\n🎲 Testing Custom Message...")
                message = input("Enter your custom message: ").strip()
                if message:
                    await test_message(client, message, "Custom Test")
                else:
                    print("❌ Please enter a message!")
                    
            elif choice == "4":
                print("\n🚀 Running all predefined tests...")
                await test_message(client, "Hello", "Testing Greeting")
                await test_message(client, "Hi there!", "Testing Another Greeting")
                await test_message(client, "Give me a quote", "Testing Quote Request")
                await test_message(client, "Inspire me", "Testing Inspiration Request")
                await test_message(client, "Motivate me please", "Testing Motivation Request")
                await test_message(client, "Random message", "Testing Default Behavior")
                print("\n✅ All tests completed!")
                
            elif choice == "5":
                print("\n👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice! Please enter 1-5.")
                
            # Ask if user wants to continue
            if choice in ["1", "2", "3"]:
                continue_choice = input("\nWould you like to test something else? (y/n): ").strip().lower()
                if continue_choice not in ['y', 'yes']:
                    print("\n👋 Goodbye!")
                    break


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())