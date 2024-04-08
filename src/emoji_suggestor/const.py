TEMPLATE = """
Task: Given the following user's text, suggest the most appropriate emoji that represents the sentiment or main idea of the message.
You should only return the emoji and no additional text.

Examples:
Input: Shielding VMs from the internet
Emoji: 🛡️

Input: Decision
Emoji: 🤝

Input: Impact
Emoji: 💥

Input: Call to action
Emoji: 📢

User text:
Input: {input}

Emoji:
"""
