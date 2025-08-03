from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI with your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class ActionOpenAIResponse(Action):
    def name(self) -> Text:
        return "action_openai_response"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Get the latest user message
        user_message = tracker.latest_message.get("text")

        try:
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )

            # Get the assistant's response
            ai_response = response.choices[0].message.content

            # Send the response back to the user
            dispatcher.utter_message(text=ai_response)

        except Exception as e:
            dispatcher.utter_message(text=f"I apologize, but I encountered an error: {str(e)}")

        return []
