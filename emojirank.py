import json
import unicodedata
import clipboard

def get_emoji_rank():
    user_input = clipboard.paste()
    # Replace newlines with commas
    converted_input = ','.join(map(str.strip, user_input.strip().split('\n')))
    # Print the converted input (optional)
    print(converted_input)
    # Load emojis from the JSON file
    emojis_file_path = "emojis.json"
    with open(emojis_file_path, 'r', encoding='utf-8') as f:
        emojis = json.load(f)
    user_input = converted_input  
    # Convert user input to list, normalize each emoji to a standard form
    user_emojis = [unicodedata.normalize('NFKC', emoji) for emoji in user_input.split(',')]
    # Find the emoji with the highest rank in the user input list
    highest_ranked_emoji = None
    highest_rank = float('inf')  # Initialize with infinity
    for emoji in user_emojis:
        if emoji in emojis:
            rank = emojis.index(emoji) + 1
            if rank < highest_rank:
                highest_ranked_emoji = emoji
                highest_rank = rank
    # Print the emoji with the highest rank and its position
    if highest_ranked_emoji:
        print("Emoji with the highest rank:", highest_ranked_emoji)
        print("Rank position:", user_emojis.index(highest_ranked_emoji) + 1)
        clipboard.copy(user_emojis.index(highest_ranked_emoji) + 1)
        return (user_emojis.index(highest_ranked_emoji) + 1)
    elif highest_ranked_emoji == None:
        print("nope")
        clipboard.copy("2")
        return 2


