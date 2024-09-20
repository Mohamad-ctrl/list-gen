import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    standalone = [
        "line status",
        "the status of my line",
        "plan I have",
        "Plan Name",
        "plan status",
        "contract status",
        "contract active",
        "contract will be renewed",
        "Contract date",
        "Benefits status",
        "the benefits associated with my plan",
        "charged for international call on this number",
        "The tariff plan"
    ]

    INTERROGATIVE_WORDS = [
        "Can", "Could", "Should", "Would", "Is", "Are", "Will", "Did", "Do", "Does", "May",
        "can be", "could be", "may be", "will be", "should be", "Do i need to be", 
        "do i have to be", "do i do", "Is being", "must i be", "shall", "shall i", "can't", 
        "cannot", "can not"
    ]

    how_phrases = [
        "how", "how does", "how to", "how can i", "how do i", "how i", "how could i", 
        "how can", "how could", "how will", "how many", "how much"
    ]

    genQa = ["What", "When", "Where", "Who", "Which", "Whom", "Whose", "Why", "what's", "what is", "what are"]


    # Define the utterance templates
    utterances = [
        "I want to know {standalone}",
        "{genQa} {standalone}",
        "{INTERROGATIVE_WORDS} {standalone}",
        "{INTERROGATIVE_WORDS} tell me {how_phrases} I will be {standalone}",
        "{standalone}",
        "show me my {standalone} please"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "standalone": standalone,
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
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
    file_name = f'standalone_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
