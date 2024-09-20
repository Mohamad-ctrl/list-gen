import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    INTERROGATIVE_WORDS = [
        "Can", "Could", "Should", "Would", "Is", "Are", "Will", "Did", "Do", "Does", "May",
        "can be", "could be", "may be", "will be", "should be", "Do i need to be", 
        "do i have to be", "do i do", "Is being", "must i be", "shall", "shall i", "can't", 
        "cannot", "can not"
    ]

    liveAgent = [
        "online conversation",
        "talk to live agent",
        "online conv",
        "a live agent",
        "live helpdesk agent",
        "speak to a real person",
        "live representative",
        "a real person",
        "chat with a human",
        "an agent",
        "live support person",
        "human rep",
        "live operator",
        "live support agent",
        "liv rep",
        "live staff member",
        "a real agent"
    ]

    # Define the utterance templates
    utterances = [
        "{liveAgent}",
        "I'd like to connect with {liveAgent} for assistance please",
        "{INTERROGATIVE_WORDS} you transfer me to {liveAgent}",
        "I need to talk to {liveAgent} if possible",
        "{INTERROGATIVE_WORDS} there an option to {liveAgent}",
        "please direct me to {liveAgent}",
        "I need to have a conversation with a {liveAgent}",
        "connect me with {liveAgent}",
        "pass me over to a {liveAgent}",
        "{INTERROGATIVE_WORDS} u provide access to {liveAgent}",
        "speaking to {liveAgent}",
        "help me connect with {liveAgent} plz"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "liveAgent": liveAgent
    }

    # Generate all combinations
    all_combinations = list(set(all_combinations))

    for utterance in utterances:
        placeholders = [f"{{{key}}}" for key in placeholder_lists if f"{{{key}}}" in utterance]
        if placeholders:
            combos = itertools.product(*(placeholder_lists[key.strip("{}")] for key in placeholders))
            for combo in combos:
                question = utterance
                for placeholder, value in zip(placeholders, combo):
                    question = question.replace(placeholder, value)
                all_combinations.append(question)
        else:
            all_combinations.append(utterance)

    all_combinations = list(set(all_combinations))
    # Save to Excel
    df = pd.DataFrame(all_combinations, columns=["Questions"])
    currentDate = datetime.now()
    
    # Format the date and time
    formatted_date_time = currentDate.strftime("%d-%m_%I.%M%p").lower()
    
    # Create the file name
    file_name = f'live_agent{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
