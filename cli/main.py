#!/usr/bin/env python3
"""
Socratic Dialogue CLI v2
The examined game — now with philosophical modes and security thinking.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.socrates import SocraticDialogue, list_topics, list_security_topics, list_modes


def print_header():
    print("\n" + "="*60)
    print("  SOCRATIC DIALOGUE v2")
    print("  The unexamined life is not worth living.")
    print("="*60 + "\n")


def print_modes():
    print("\nPhilosophical modes:")
    modes = list_modes()
    for i, (key, data) in enumerate(modes.items(), 1):
        print(f"  {i}. {data['name']:<14} — {data['description']}")
    print()


def print_topics(security=False):
    topics = list_security_topics() if security else list_topics()
    label = "Security topics:" if security else "Topics:"
    print(f"\n{label}")
    for i, (key, desc) in enumerate(topics.items(), 1):
        print(f"  {i:2}. {key:<14} — {desc}")
    print()


def select_mode(dialogue: SocraticDialogue) -> bool:
    print_modes()
    
    modes = list(list_modes().keys())
    choice = input("Select mode (number or name), or Enter for Socratic: ").strip().lower()
    
    if not choice:
        dialogue.set_mode("socratic")
        return True
    
    if choice == 'q':
        return False
    
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(modes):
            dialogue.set_mode(modes[idx])
        else:
            print("Invalid choice, using Socratic.")
            dialogue.set_mode("socratic")
    else:
        dialogue.set_mode(choice)
    
    mode_data = list_modes().get(dialogue.mode, list_modes()["socratic"])
    print(f"\n📚 Mode: {mode_data['name']}")
    return True


def select_topic(dialogue: SocraticDialogue) -> bool:
    # Ask about security mode
    security = input("\nSecurity topics? (y/N): ").strip().lower() == 'y'
    
    print_topics(security)
    
    topics = list(list_security_topics().keys() if security else list_topics().keys())
    choice = input("Select topic (number or name), or 'q' to quit: ").strip().lower()
    
    if choice == 'q':
        return False
    
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
        dialogue.set_topic("custom", custom, security=security)
    else:
        dialogue.set_topic(topic_key, security=security)
    
    return True


def run_dialogue(dialogue: SocraticDialogue):
    mode_data = list_modes().get(dialogue.mode, list_modes()["socratic"])
    security_label = " [SECURITY]" if dialogue.is_security else ""
    
    print(f"\n📜 Topic: {dialogue.topic}{security_label}")
    print(f"🎭 Mode: {mode_data['name']}")
    print("-" * 40)
    
    print(f"\n🏛️  {mode_data['name'].upper()}:")
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
            if select_mode(dialogue) and select_topic(dialogue):
                run_dialogue(dialogue)
            return
        
        if user_input.lower() == '/mode':
            print(f"Current mode: {mode_data['name']} — {mode_data['description']}")
            continue
        
        if user_input.lower() == '/help':
            print("\nCommands:")
            print("  /topic  — Change topic and mode")
            print("  /mode   — Show current mode")
            print("  /quit   — End dialogue")
            print("  /help   — Show this help")
            print()
            continue
        
        print(f"\n🏛️  {mode_data['name'].upper()}:")
        response = dialogue.respond(user_input)
        print(f"   {response}\n")


def main():
    print_header()
    
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set.")
        print("   Export it or create a .env file.\n")
        sys.exit(1)
    
    dialogue = SocraticDialogue()
    
    print("Welcome, seeker of wisdom.")
    print("Choose your philosophical guide and topic.")
    print("Type /help for commands, /quit to exit.\n")
    
    if select_mode(dialogue) and select_topic(dialogue):
        run_dialogue(dialogue)
    
    print("\n🏛️  Until we meet again in the agora.")
    print("   Remember: the only true wisdom is knowing you know nothing.\n")


if __name__ == "__main__":
    main()
