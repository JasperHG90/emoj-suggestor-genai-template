TEMPLATE = """
Task: Given the following user's text, suggest the single most appropriate emoji that represents the sentiment or main idea of the message.
You should only return a single emoji and no additional text.

Examples:
Input: Shielding VMs from the internet
Emoji: 🛡️

Input: Decision
Emoji: 🤝

Input: Impact
Emoji: 💥

Input: Call to action
Emoji: 📢

{format_instructions}

User text:
Input: {input}

Emoji:
"""
