#!/usr/bin/env python3
"""
Socratic Dialogue CLI
The examined game, in your terminal.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.socrates import SocraticDialogue, list_topics


def print_header():
    print("\n" + "="*60)
    print("  SOCRATIC DIALOGUE")
    print("  The unexamined life is not worth living.")
    print("="*60 + "\n")


def print_topics():
    print("\nAvailable topics:")
    topics = list_topics()
    for i, (key, desc) in enumerate(topics.items(), 1):
        print(f"  {i:2}. {key:<12} — {desc}")
    print()


def select_topic(dialogue: SocraticDialogue) -> bool:
    print_topics()
    
    topics = list(list_topics().keys())
    choice = input("Select topic (number or name), or 'q' to quit: ").strip().lower()
    
    if choice == 'q':
        return False
    
    # Handle numeric choice
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(topics):
            topic_key = topics[idx]
        else:
            print("Invalid choice.")
            return select_topic(dialogue)
    else:
        topic_key = choice
    
    if topic_key == "custom":
        custom = input("Enter your question: ").strip()
        dialogue.set_topic("custom", custom)
    else:
        dialogue.set_topic(topic_key)
    
    return True


def run_dialogue(dialogue: SocraticDialogue):
    print(f"\n📜 Topic: {dialogue.topic}\n")
    print("-" * 40)
    
    # Get opening from Socrates
    print("\n🏛️  SOCRATES:")
    opening = dialogue.get_opening()
    print(f"   {opening}\n")
    
    while True:
        try:
            user_input = input("📝 YOU: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n")
            break
        
        if not user_input:
            continue
        
        if user_input.lower() in ['/quit', '/q', '/exit']:
            break
        
        if user_input.lower() in ['/topic', '/new']:
            dialogue.reset()
            if select_topic(dialogue):
                run_dialogue(dialogue)
            return
        
        if user_input.lower() == '/help':
            print("\nCommands:")
            print("  /topic  — Change topic")
            print("  /quit   — End dialogue")
            print("  /help   — Show this help")
            print()
            continue
        
        print("\n🏛️  SOCRATES:")
        response = dialogue.respond(user_input)
        print(f"   {response}\n")


def main():
    print_header()
    
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set.")
        print("   Export it or create a .env file.\n")
        sys.exit(1)
    
    dialogue = SocraticDialogue()
    
    print("Welcome, seeker of wisdom.")
    print("Type /help for commands, /quit to exit.\n")
    
    if select_topic(dialogue):
        run_dialogue(dialogue)
    
    print("\n🏛️  Until we meet again in the agora.")
    print("   Remember: the only true wisdom is knowing you know nothing.\n")


if __name__ == "__main__":
    main()
