import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    homepackages = [
        "home TV services", "home TV packages", "TV channels", "TV support channels",
        "TV service", "TV package", "TV packages", "subscribe to TV packages",
        "subscribed TV Packages", "TV services", "TV", "Television packages",
        "TV plan", "TV subscription", "manage my home TV packages",
        "manage my current TV package", "modify my home TV package", 
        "customize my TV package", "adjust my home TV package",
        "add new channels to my TV package", "add sports channels to my TV package",
        "remove channels from my current TV package", "modify my TV package to include HD channels"
    ]

    cost_list = ["cost", "fee", "fees", "payment", "charges"]

    StreamingServicesInquiry = [
        "activate", "active", "subscribe", "subscription", "subscribe to", "subscribed",
        "want to have", "deactivate", "cancel", "unsubscribe", "delete", "remove",
        "have a problem with", "there is an issue with", "i have an issue with"
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

    StreamingSerType = ["OSN", "osn streaming", "Disney Plus", "Disney+", "Amazon Prime"]

    relocate = [
        "relocate my Home services", "home relocation", "moving to a new home", "move my Home services",
        "moving into a new home", "move to a new home", "moving to a new house", "relocated to a new house",
        "new home", "transfer to a new home", "new home address", "moving home internet", "new home location",
        "relocation", "change my home location", "relocate my home connection to a new address",
        "transfer my home connection to a different location", "change the address for my home connection",
        "update my home connection with my new address", "switch my home connection to a new house"
    ]

    subscribear = ["subscribe to", "subscribed", "apply", "subscription", "sign up", "set", "get", "purchase", "set up", "buy"]

    # Define the utterance templates
    utterances = [
        "I am looking for {homepackages}",
        "{homepackages}",
        "I want to {subscribear} {homepackages}",
        "{how_phrases}  {INTERROGATIVE_WORDS} I {homepackages}?",
        "{how_phrases}  {INTERROGATIVE_WORDS} I check my {homepackages} on My Account?",
        "{genQa} channels are available with do {homepackages}?",
        "I am looking for do {homepackages} list",
        "{how_phrases} search for {homepackages} on do App?",
        "{how_phrases} check my do {homepackages}?",
        "{genQa} options {INTERROGATIVE_WORDS} I have for {homepackages}",
        "i want {homepackages}",
        "{how_phrases} I {homepackages} online?",
        "{INTERROGATIVE_WORDS} you help me {homepackages}?",
        "Streaming services {cost}",
        "{StreamingSerType}",
        "{how_phrases}  {INTERROGATIVE_WORDS} I {StreamingServicesInquiry} {StreamingSerType}",
        "{how_phrases} {StreamingServicesInquiry} {StreamingSerType}?",
        "i want to {StreamingServicesInquiry} {StreamingSerType}",
        "i am {StreamingServicesInquiry} {StreamingSerType}",
        "{how_phrases} to get offer to {StreamingServicesInquiry} {StreamingSerType}?",
        "{INTERROGATIVE_WORDS} you help me to {StreamingServicesInquiry} {StreamingSerType} on do app",
        "do offers {StreamingSerType}",
        "looking for {StreamingSerType} {cost}",
        "If I am an existing do customer, {INTERROGATIVE_WORDS} I {StreamingServicesInquiry} plan that has {StreamingSerType}?",
        "{genQa} streaming services do you offer",
        "{INTERROGATIVE_WORDS} I access any streaming services through do",
        "{StreamingSerType} you support popular streaming services",
        "I need information about the available streaming services",
        "{INTERROGATIVE_WORDS} there any special deals for streaming services offered here",
        "{how_phrases} {INTERROGATIVE_WORDS}  I {relocate}?",
        "{how_phrases} move my home services to a {relocate}?",
        "I am {relocate}. {how_phrases} move my home Services",
        "{relocate} my fixed Services",
        "I want to {relocate}.",
        "{how_phrases} transfer my do home connection to a {relocate}",
        "i want to apply for {relocate}",
        "{relocate} {cost}",
        "{how_phrases} send {relocate} request",
        "I'm planning to {relocate} and i need your help",
        "{INTERROGATIVE_WORDS} i {relocate}"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "homepackages": homepackages,
        "cost": cost_list,
        "StreamingServicesInquiry": StreamingServicesInquiry,
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
        "StreamingSerType": StreamingSerType,
        "relocate": relocate,
        "subscribear": subscribear
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
    file_name = f'generated_questions_for_home_services_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
