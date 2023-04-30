import openai
import telebot
from langdetect import detect

bot = telebot.TeleBot('TELETOKEN')

# Set OpenAI API key
openai.api_key = "AITOKEN"

# Define a function to get response from OpenAI API
def get_response(text, lang):
    try:
        # Call OpenAI API with the given question and language
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=(f"Answer the following question in {lang}:\n{text}\n\nAnswer:"),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Return the response text
        return response.choices[0].text.strip()
    except Exception as e:
        # Handle any errors that occur while calling the API
        print(f"Error while calling OpenAI API: {e}")
        return "I'm sorry, I could not process your request at the moment."

# Define a message handler to reply to user messages
@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
    if message.text:
        # Get the user's question and detect its language
        question = message.text
        lang = detect(question)

        # Get a response from OpenAI API using the question and language
        answer = get_response(question, lang)

        # Reply to the user's message with the answer
        bot.reply_to(message, answer)

# Start the bot and listen for incoming messages
bot.polling()
