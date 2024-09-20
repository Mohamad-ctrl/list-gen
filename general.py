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

    # Define the utterance templates
    utterances = [
    "Main menu",
    "services list",
    "list of services",
    "i want to back to the main menu",
    "where is the main menu",
    "show me the menu",
    "how to back to the main menu",
    "Different number",
    "i have another number",
    "i want to enter a different mobile number",
    "{INTERROGATIVE_WORDS} enter another mobile number",
    "end the session",
    "stop",
    "send another otp",
    "this one expired send me another otp",
    "otp expired regenrate another one please",
    "nothing for now",
    "no",
    "thank you",
    "bye",
    "nothing thanks",
    "i don't want anything",
    "i have no other question",
    "nope",
    "yes",
    "yup i have another question",
    "yes need further help",
    "yeah want to ask you something else",
    "i want another help",
    "there is another question"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
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
    file_name = f'general_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
