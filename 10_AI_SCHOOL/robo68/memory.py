# memory.py
"""
Conversation memory buffer and summary.
Keeps recent dialogue history and can produce a summary if needed.
"""

from collections import deque

class Memory:
    def __init__(self, max_buffer: int = 5):
        """
        :param max_buffer: number of recent exchanges to keep.
        """
        self.max_buffer = max_buffer
        # Deque of tuples: (user_message, bot_response)
        self.buffer = deque(maxlen=max_buffer)
    
    def add(self, user_msg: str, bot_msg: str):
        """
        Add a new user-bot exchange to memory.
        """
        self.buffer.append((user_msg, bot_msg))
    
    def get_buffer_text(self) -> str:
        """
        Return the recent conversation as a single string (user: .. bot: ..).
        """
        parts = []
        for user, bot in self.buffer:
            parts.append(f"User: {user}")
            parts.append(f"Bot: {bot}")
        return "\n".join(parts)
    
    def summary(self) -> str:
        """
        (Optional) Return a high-level summary of memory for context.
        Placeholder for actual summarization logic.
        """
        if not self.buffer:
            return ""
        # Example: just mention topics of last exchanges
        topics = " ".join([u.split()[0] for (u, _) in self.buffer])
        return f"(Recent topics: {topics})"

# Example usage:
# mem = Memory()
# mem.add("Hello", "Hi there!")
# mem.add("I have a question.", "Sure, ask me anything.")
# print(mem.get_buffer_text())
