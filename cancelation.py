import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    canceltype = [
        "my prepaid plan",
        "my postpaid plan",
        "my mobile plan",
        "my prepaid home plan",
        "home wireless plan",
        "home wireless 5G plan",
        "home wireless 4G plan",
        "home services",
        "fixed plan",
        "home fiber plan",
        "my bundles",
        "my active bundles",
        "all bundles",
        "value added services",
        "vas"
    ]


    cancelBundleType = [
        "my data plan",
        "my data bundles",
        "my voice plan",
        "voice bundles",
        "minutes bundles",
        "my du special offer subscription",
        "my offers",
        "my internet calling bundles"
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

    cancellationreason = [
        "too expensive",
        "The monthly fees are too high",
        "prices have become unaffordable",
        "the high costs",
        "charges are too much",
        "The prices are too expensive",
        "I want to relocate",
        "I'm relocating",
        "I'm moving out of the country",
        "I'm emigrating",
        "moving to a different state",
        "I found a better offer",
        "I'm switching providers",
        "leaving the country",
        "looking for a better deal",
        "found a more affordable option elsewhere",
        "Service dissatisfaction",
        "I am not happy with your services",
        "I'm extremely unhappy with your service",
        "Your company's service has been terrible",
        "poor quality of services",
        "service has been a complete disappointment",
        "dissatisfied with the service",
        "The service I'm receiving is unacceptable",
        "I no longer need my current plan",
        "I have another reason"
    ]


    cancel = [
        "cancelation",
        "delete",
        "cancel",
        "remove",
        "shut down",
        "drop",
        "deactivate",
        "unsubscribe to",
        "unsubscription",
        "cancellation request",
        "discontinue",
        "end",
        "Terminate",
        "Stop",
        "Disconnect",
        "Disable",
        "Cease",
        "Suspend",
        "Cut off",
        "deactivation",
        "removing",
        "ending",
        "service cancellation",
        "ending the services",
        "end my contract",
        "canceling"
    ]

    # Define the utterance templates
    utterances = [
        "{cancel} {canceltype}",
        "{cancel}",
        "{cancellationreason} so I want to {cancel} {canceltype}",
        "{cancel} my current plans",
        "{how_phrases} {cancel} my {canceltype}?",
        "{how_phrases} {INTERROGATIVE_WORDS} I {cancel}?",
        "I want to {cancel} {cancelBundleType}",
        "{how_phrases} {INTERROGATIVE_WORDS} I {cancel} {canceltype} through My Account?",
        "{INTERROGATIVE_WORDS} I {cancel} my {cancelBundleType}",
        "Help me to {cancel} my {canceltype} because {cancellationreason}",
        "{cancellationreason} and I want to {cancel}",
        "{cancelBundleType}",
        "{how_phrases} {INTERROGATIVE_WORDS} I {cancelBundleType}",
        "Help me, I want to {cancelBundleType}",
        "{cancelBundleType}",
        "{cancel} all subscriptions",
        "{cancelBundleType} {cancellationreason}",
        "{INTERROGATIVE_WORDS} you walk me through the steps to {cancel} my {canceltype}",
        "{how_phrases} I go about {cancel} my existing contract",
        "I demand to cancel my telecom services"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "canceltype": canceltype,
        "cancelBundleType": cancelBundleType,
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
        "cancellationreason": cancellationreason,
        "cancel": cancel,
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
    file_name = f'cancelation_tes{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
