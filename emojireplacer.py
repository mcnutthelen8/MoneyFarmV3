import json
import unicodedata
import clipboard

def emojireplce():
    def convert_input(input_string):
        lines = input_string.strip().split('\n')
        emojis = []
        percentages = []
        for i in range(0, len(lines), 2):
            emoji = lines[i].strip()
            if i + 1 < len(lines):
                percent = lines[i + 1].strip()
                percentages.append(float(percent.rstrip('%')))
            else:
                print("Invalid input format. Percentage missing for an emoji.")
                return None, None

            emojis.append(emoji)

        if not percentages:
            print("No valid percentage values found.")
            return None, None

        max_percent_index = percentages.index(max(percentages))
        return emojis, max_percent_index

    def ordinal_suffix(n):
        if 11 <= n % 100 <= 13:
            return f"{n}th"
        else:
            return f"{n}{['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]}"

    # Example input
    input_string = clipboard.paste() 

    # User input
    user_emojis, max_percent_index = convert_input(input_string)
    if user_emojis is None:
        exit()

    # Load emojis from the JSON file
    emojis_file_path = 'emojis.json'
    with open(emojis_file_path, 'r', encoding='utf-8') as f:
        emojis_list = json.load(f)

    # Normalize each emoji to a standard form
    user_emojis = [unicodedata.normalize('NFKC', emoji) for emoji in user_emojis]

    # Ensure all user input emojis exist in the JSON list
    for emoji in user_emojis:
        if emoji not in emojis_list:
            print(f"Emoji {emoji} not found in the JSON list. Adding it to the list.")
            emojis_list.append(emoji)

    # Get the emoji with the highest score
    chosen_emoji = user_emojis[max_percent_index]

    # Find the lowest rank emoji among the user input emojis
    user_input_rank_positions = [emojis_list.index(emoji) for emoji in user_emojis]
    lowest_rank_position = min(user_input_rank_positions)
    lowest_rank_emoji = user_emojis[user_input_rank_positions.index(lowest_rank_position)]

    # Check if chosen emoji is already in the correct position
    chosen_emoji_index = emojis_list.index(chosen_emoji)
    lowest_rank_emoji_index = emojis_list.index(lowest_rank_emoji)

    if chosen_emoji_index < lowest_rank_emoji_index:
        print("Emojis are already in the correct order.")
    else:
        # Move the chosen emoji to the position before the lowest rank emoji
        emojis_list.remove(chosen_emoji)
        emojis_list.insert(lowest_rank_emoji_index, chosen_emoji)
        print("Emojis reordered.")

    # Save the updated emojis list back to the JSON file
    with open(emojis_file_path, 'w', encoding='utf-8') as f:
        json.dump(emojis_list, f, ensure_ascii=False)

    # Print the updated list
    print("\nAfter the script, JSON list:")
    print(emojis_list)

    # Print the chosen emoji and its new position
    print(f"""
    User input: {user_emojis}
    Chosen emoji: {chosen_emoji} ({ordinal_suffix(max_percent_index + 1)} emoji)
    Lowest rank emoji: {lowest_rank_emoji} ({ordinal_suffix(lowest_rank_position + 1)} emoji)
    Position of chosen emoji after reordering: {emojis_list.index(chosen_emoji) + 1}
    """)
