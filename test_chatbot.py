#!/usr/bin/env python3
"""
Test script for the Rule-Based Chatbot
This script demonstrates various chatbot capabilities without requiring user interaction.
Perfect for presentations and demonstrations.
"""

from chatbot import RuleBasedChatbot
import time

def test_chatbot_responses():
    """
    Test various chatbot responses to demonstrate functionality.
    """
    print("=" * 60)
    print("🧪 RULE-BASED CHATBOT TESTING SUITE")
    print("=" * 60)
    print()
    
    # Initialize the chatbot
    chatbot = RuleBasedChatbot()
    
    # Test cases organized by category
    test_cases = [
        {
            'category': '👋 Greetings',
            'inputs': ['hello', 'hi there', 'good morning', 'hey']
        },
        {
            'category': '🤔 Identity Questions',
            'inputs': ['who are you', 'what are you', 'your name', 'introduce yourself']
        },
        {
            'category': '❓ How are you',
            'inputs': ['how are you', 'how do you feel', 'what\'s up']
        },
        {
            'category': '💪 Capabilities',
            'inputs': ['what can you do', 'help me', 'your abilities']
        },
        {
            'category': '😄 Jokes',
            'inputs': ['tell me a joke', 'make me laugh', 'something funny']
        },
        {
            'category': '🌤️ Weather',
            'inputs': ['weather', 'is it raining', 'sunny today']
        },
        {
            'category': '💻 Technology',
            'inputs': ['python', 'programming', 'artificial intelligence']
        },
        {
            'category': '🕐 Time',
            'inputs': ['what time is it', 'current time', 'time']
        },
        {
            'category': '💝 Compliments',
            'inputs': ['you are great', 'awesome', 'amazing job']
        },
        {
            'category': '🙏 Thanks',
            'inputs': ['thank you', 'thanks', 'appreciate it']
        },
        {
            'category': '❌ Unknown Input',
            'inputs': ['xyz123', 'random stuff', 'blah blah blah']
        },
        {
            'category': '👋 Farewells',
            'inputs': ['goodbye', 'bye', 'see you later']
        }
    ]
    
    total_tests = 0
    
    for test_group in test_cases:
        print(f"\n{test_group['category']}")
        print("-" * 40)
        
        for user_input in test_group['inputs']:
            total_tests += 1
            print(f"👤 Input: '{user_input}'")
            
            # Get response from chatbot
            response = chatbot.get_response(user_input)
            print(f"🤖 Response: {response}")
            print()
            
            # Small delay for readability
            time.sleep(0.5)
    
    print("=" * 60)
    print(f"✅ Testing completed! Processed {total_tests} test cases.")
    print("=" * 60)

def test_pattern_matching():
    """
    Test the pattern matching functionality specifically.
    """
    print("\n🔍 PATTERN MATCHING TESTS")
    print("=" * 40)
    
    chatbot = RuleBasedChatbot()
    
    pattern_tests = [
        ('hello world', 'greetings'),
        ('goodbye everyone', 'farewells'),
        ('how are you doing', 'how_are_you'),
        ('tell me a joke please', 'jokes'),
        ('what is the weather like', 'weather'),
        ('I love python programming', 'technology'),
        ('thank you so much', 'thanks'),
        ('you are amazing', 'compliments'),
        ('random gibberish', None),  # Should return None
    ]
    
    for test_input, expected_category in pattern_tests:
        result = chatbot.find_pattern_match(test_input)
        status = "✅" if result == expected_category else "❌"
        print(f"{status} Input: '{test_input}' → Expected: {expected_category}, Got: {result}")
    
    print("\n🔍 Pattern matching tests completed!")

def demonstrate_conversation_flow():
    """
    Demonstrate a realistic conversation flow.
    """
    print("\n💬 CONVERSATION FLOW DEMONSTRATION")
    print("=" * 50)
    
    chatbot = RuleBasedChatbot()
    
    # Simulate a realistic conversation
    conversation = [
        "Hello!",
        "How are you?",
        "What can you do?",
        "Tell me a joke",
        "That's funny! You're amazing",
        "What's the weather like?",
        "Do you know Python?",
        "Thank you for chatting",
        "Goodbye!"
    ]
    
    print("🎭 Simulating a realistic conversation:")
    print("-" * 40)
    
    for i, user_input in enumerate(conversation, 1):
        print(f"\n[Exchange {i}]")
        print(f"👤 User: {user_input}")
        
        response = chatbot.get_response(user_input)
        print(f"🤖 Bot: {response}")
        
        time.sleep(1)  # Pause for readability
    
    print(f"\n✨ Conversation completed with {len(conversation)} exchanges!")

def main():
    """
    Run all test functions.
    """
    print("🚀 Starting comprehensive chatbot testing...\n")
    
    # Run all tests
    test_chatbot_responses()
    test_pattern_matching()
    demonstrate_conversation_flow()
    
    print("\n🎉 All tests completed successfully!")
    print("\n💡 To run the interactive chatbot, use: python chatbot.py")

if __name__ == "__main__":
    main()