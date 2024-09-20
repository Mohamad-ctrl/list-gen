import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    switch = [
        "change my plan",
        "upgrade my plan",
        "downgrade my plan",
        "Plan Migration",
        "switch my plan",
        "switch to another plan",
        "migrate to a new plan",
        "changing my plan",
        "upgrade or downgrade"
    ]

    switchType = [
        "Switch to du",
        "switch my number to du",
        "switching to du",
        "shift my number to du",
        "transformation my number to du",
        "transformation to du",
        "convert my number to du",
        "converting to du",
        "change my mobile plan",
        "switch my mobile plan",
        "upgrade my mobile plan",
        "switching my mobile plan",
        "change the plan of my mobile",
        "changing my mobile plan",
        "switch my home internet plan",
        "switch to a different fixed plan",
        "upgrading my fixed plan",
        "switch home services plan",
        "switch home plan",
        "downgrade my fixed plan",
        "change my fixed plan to a different option",
        "switching home plan",
        "migrate from du home plan to Home Wireless Plan",
        "switch my account from a Business plan to a Personal plan",
        "switching from Business to Personal plan",
        "downgrade my plan from Business to Personal",
        "convert my current Business plan to a Personal plan",
        "changing my plan from Business to Personal",
        "transition from enterprise to a Personal plan",
        "enterprise to personal",
        "alter my subscription from a Business plan to a Personal plan",
        "transfer from current Business plan to a Personal plan",
        "Change Enterprise to Consumer"
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

    switchMobileType = [
        "Change Prepaid plan",
        "switch my prepaid plan",
        "change my current prepaid package",
        "upgrade my prepaid plan",
        "downgrade my prepaid plan",
        "switch to another prepaid plan",
        "Change Postpaid plan",
        "switch my postpaid plan",
        "upgrade my postpaid plan",
        "downgrade my postpaid plan",
        "switch to a different postpaid plan",
        "swap my prepaid plan to postpaid plan",
        "switch from my current postpaid plan to a prepaid option",
        "move from a prepaid plan to a postpaid plan",
        "change my mobile plan from postpaid to prepaid",
        "converting my prepaid plan to a postpaid one",
        "migrate from postpaid to prepaid",
        "downgrade from postpaid to prepaid",
        "upgrade from prepaid to postpaid",
        "Post to Pre",
        "Pre to Post"
    ]

    # Define the utterance templates
    utterances = [
        "{switchType}",
        "{switch}",
        "{switchMobileType}",
        "Help me to {switchType}",
        "{INTERROGATIVE_WORDS} i {switch}",
        "{INTERROGATIVE_WORDS} I {switchMobileType}",
        "i'd like to {switchMobileType}",
        "I want to {switch}",
        "{how_phrases} {switch}",
        "steps {INTERROGATIVE_WORDS} to {switchType}",
        "{how_phrases} {switchType}",
        "{genQa} i have to do to {switchType} {switchMobileType}",
        "I'm interested in {switchType}",
        "{genQa} the steps involved in {switchType}",
        "I need assistance in {switchType}"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "switch": switch,
        "switchType": switchType,
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
        "switchMobileType": switchMobileType
    }

    # Generate all combinations
    all_combinations = []

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
    file_name = f'Migration_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
