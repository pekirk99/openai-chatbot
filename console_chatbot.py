import openai
import json

def load_config():
    """
    Load API configuration from a JSON file.
    """
    try:
        with open("config.json", "r") as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Error loading config.json: {e}")
        return {}

def get_chatgpt_response(prompt, api_key):
    """
    Sends a prompt to OpenAI's ChatGPT and retrieves the response.
    """
    try:
        openai.api_key = api_key
        response = openai.chat.completions.create(
            messages=[{
                "role": "user",
                "content": prompt,
            }],
            model="gpt-4o-mini",
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    """
    Main loop for the console chatbot.
    """
    config = load_config()
    api_key = config.get("OPENAI_API_KEY")

    if not api_key:
        print("API key not found in config.json. Please add your OpenAI API key.")
        return

    print("\nWelcome to the Console Chatbot! Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = get_chatgpt_response(user_input, api_key)
        print(f"ChatGPT: {response}\n")

if __name__ == "__main__":
    main()
