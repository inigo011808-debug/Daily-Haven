"""Editorial content for the site that isn't menu data."""

from datetime import time

# "Overheard at the counter" fragments. Times are real time objects so they
# get formatted by the `ampm` filter in app.py rather than hardcoded strings.
OVERHEARD_LINES = [
    {"time": time(6, 45), "quote": "Did you find parking or are you still circling?"},
    {"time": time(7, 12), "quote": "Same order, but tell me about your weekend first."},
    {"time": time(8, 3), "quote": "Wait, is this the oat one or is that yours?"},
    {"time": time(9, 26), "quote": "She said ten, so I'm reading until eleven."},
    {"time": time(10, 40), "quote": "Can we take this table for the book club again?"},
    {"time": time(11, 15), "quote": "I'll get this one. You got Tuesday."},
    {"time": time(15, 0), "quote": "Sorry, what was I saying?"},
    {"time": time(16, 5), "quote": "One more and then I really do have to go."},
    {"time": time(17, 30), "quote": "My laptop is at four percent, so this is a countdown."},
]

# Short note under each menu category heading.
CATEGORY_NOTES = {
    "Coffee": "Roasted in small batches, every Tuesday.",
    "Tea & Non-Caf": "For the second half of the conversation.",
    "Pastries": "Baked fresh each morning, local suppliers.",
    "Light Bites": "Small plates to share or enjoy alone.",
}
