import random
import re
from datetime import datetime

class RuleBasedChatbot:
    """
    A simple rule-based chatbot that responds to user inputs using predefined patterns and responses.
    This chatbot demonstrates basic natural language processing concepts and conversation flow.
    """
    
    def __init__(self):
        # Define patterns and their corresponding responses
        self.patterns = {
            'greetings': {
                'patterns': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
                'responses': [
                    "Hello there! How can I help you today?",
                    "Hi! Nice to meet you!",
                    "Hey! What's on your mind?",
                    "Greetings! I'm here to chat with you.",
                    "Hello! I'm excited to talk with you!"
                ]
            },
            'farewells': {
                'patterns': ['bye', 'goodbye', 'see you', 'farewell', 'quit', 'exit'],
                'responses': [
                    "Goodbye! Have a wonderful day!",
                    "See you later! Take care!",
                    "Bye! It was nice chatting with you!",
                    "Farewell! Come back anytime!",
                    "Take care! Hope to see you again soon!"
                ]
            },
            'how_are_you': {
                'patterns': ['how are you', 'how do you feel', 'how\'s it going', 'what\'s up'],
                'responses': [
                    "I'm doing great, thank you for asking!",
                    "I'm functioning perfectly and ready to help!",
                    "I'm just a program, but I'm working well!",
                    "All systems running smoothly! How are you?",
                    "I'm excellent! Thanks for caring about a chatbot's wellbeing!"
                ]
            },
            'identity': {
                'patterns': ['who are you', 'what are you', 'your name', 'introduce yourself'],
                'responses': [
                    "I'm a rule-based chatbot created for learning purposes!",
                    "I'm your friendly neighborhood chatbot, here to help!",
                    "I'm a simple AI assistant built with Python!",
                    "I'm a chatbot designed to demonstrate conversation patterns!",
                    "I'm an artificial conversational agent, nice to meet you!"
                ]
            },
            'capabilities': {
                'patterns': ['what can you do', 'your abilities', 'help me', 'what do you know'],
                'responses': [
                    "I can chat about various topics, tell jokes, answer basic questions, and keep you company!",
                    "I can respond to greetings, share information, tell jokes, and have simple conversations!",
                    "I'm good at chatting, answering questions, and providing basic assistance!",
                    "I can help with simple queries, tell jokes, and engage in friendly conversation!"
                ]
            },
            'jokes': {
                'patterns': ['tell me a joke', 'joke', 'make me laugh', 'something funny'],
                'responses': [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Why did the scarecrow win an award? He was outstanding in his field!",
                    "Why don't eggs tell jokes? They'd crack each other up!",
                    "What do you call a fake noodle? An impasta!",
                    "Why did the math book look so sad? Because it had too many problems!"
                ]
            },
            'weather': {
                'patterns': ['weather', 'is it raining', 'sunny', 'cloudy', 'temperature'],
                'responses': [
                    "I can't check real-time weather, but you can try a weather app or website!",
                    "I don't have access to weather data, but I hope it's nice where you are!",
                    "Sorry, I can't provide weather updates. Try checking your local weather service!",
                    "I wish I could tell you about the weather, but I'm limited to text conversations!"
                ]
            },
            'technology': {
                'patterns': ['python', 'programming', 'coding', 'computer', 'technology', 'ai'],
                'responses': [
                    "Python is an amazing programming language! This chatbot is built with it!",
                    "I love talking about technology! Programming is fascinating!",
                    "Technology is incredible! It allows us to have this conversation!",
                    "Programming languages like Python make creating chatbots possible!",
                    "AI and programming are exciting fields with endless possibilities!"
                ]
            },
            'time': {
                'patterns': ['time', 'what time is it', 'current time', 'clock'],
                'responses': [
                    f"The current time is {datetime.now().strftime('%H:%M:%S')}",
                    f"It's {datetime.now().strftime('%I:%M %p')} right now!",
                    f"The time is {datetime.now().strftime('%H:%M')} on {datetime.now().strftime('%B %d, %Y')}"
                ]
            },
            'compliments': {
                'patterns': ['you are good', 'you are great', 'awesome', 'amazing', 'wonderful'],
                'responses': [
                    "Thank you so much! That's very kind of you to say!",
                    "You're too kind! I'm just doing my best to help!",
                    "That means a lot to me! You're pretty awesome yourself!",
                    "Thank you! I'm glad you're enjoying our conversation!",
                    "You're making my circuits happy! Thank you!"
                ]
            },
            'thanks': {
                'patterns': ['thank you', 'thanks', 'appreciate', 'grateful'],
                'responses': [
                    "You're very welcome! Happy to help!",
                    "No problem at all! That's what I'm here for!",
                    "My pleasure! Feel free to ask anything else!",
                    "You're welcome! I enjoy helping you!",
                    "Glad I could help! Anything else I can do for you?"
                ]
            }
        }
        
        # Default responses for unrecognized input
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "That's interesting! Can you tell me more?",
            "I'm still learning. Can you try asking in a different way?",
            "Hmm, I don't have a good response for that. What else would you like to talk about?",
            "I'm not quite sure how to respond to that. Try asking me something else!",
            "That's beyond my current knowledge. Is there something else I can help with?"
        ]
    
    def find_pattern_match(self, user_input):
        """
        Find the best matching pattern for the user input.
        Returns the category name if a match is found, None otherwise.
        """
        user_input = user_input.lower().strip()
        
        for category, data in self.patterns.items():
            for pattern in data['patterns']:
                # Use word boundaries for better matching
                if re.search(r'\b' + re.escape(pattern) + r'\b', user_input):
                    return category
        return None
    
    def get_response(self, user_input):
        """
        Generate an appropriate response based on the user input.
        """
        category = self.find_pattern_match(user_input)
        
        if category:
            return random.choice(self.patterns[category]['responses'])
        else:
            return random.choice(self.default_responses)
    
    def start_conversation(self):
        """
        Main conversation loop for the chatbot.
        """
        print("🤖 Chatbot: Hello! I'm an advanced rule-based chatbot.")
        print("🤖 Chatbot: I can chat about various topics, tell jokes, and answer questions!")
        print("🤖 Chatbot: Type 'bye', 'quit', or 'exit' to end our conversation.\n")
        
        conversation_count = 0
        
        while True:
            try:
                user_input = input("👤 You: ").strip()
                
                if not user_input:
                    print("🤖 Chatbot: I didn't catch that. Please say something!")
                    continue
                
                conversation_count += 1
                
                # Check for farewell patterns
                if self.find_pattern_match(user_input) == 'farewells':
                    print(f"🤖 Chatbot: {self.get_response(user_input)}")
                    print(f"🤖 Chatbot: We had {conversation_count} exchanges. Thanks for chatting!")
                    break
                
                # Generate and display response
                response = self.get_response(user_input)
                print(f"🤖 Chatbot: {response}")
                
            except KeyboardInterrupt:
                print("\n🤖 Chatbot: Goodbye! Thanks for the chat!")
                break
            except Exception as e:
                print(f"🤖 Chatbot: Oops! Something went wrong. Let's keep chatting!")

def main():
    """
    Main function to run the chatbot.
    """
    chatbot = RuleBasedChatbot()
    chatbot.start_conversation()

if __name__ == "__main__":
    main()