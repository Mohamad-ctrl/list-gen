import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    bundleType = [
        "data package",
        "mobile internet bundle",
        "packages of internet access",
        "data packs",
        "voice package",
        "voice minutes bundle",
        "voice packs",
        "minutes bundles",
        "minutes packs",
        "voice mins",
        "roaming plans",
        "roaming data",
        "roaming services",
        "international roaming",
        "traveling bundle",
        "roaming package",
        "plans of roaming",
        "Internet calling pack",
        "Internet calling bundle",
        "BOTIM pack",
        "VOICO pack"
    ]

    voiceType = [
        "national minutes",
        "local minutes",
        "minutes inside UAE",
        "UAE minutes",
        "calls inside UAE",
        "national callings",
        "international minutes",
        "calling minutes international",
        "calls outside UAE",
        "international callings"
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

    checkFix = [
        "Voice minutes Check & Fix",
        "Data Check & Fix",
        "Voice mins Check & Fix",
        "data bundles check & fix"
    ]

    specialdeals = [
        "special deals",
        "special offer",
        "all special offers",
        "months special offer",
        "new special offer",
        "promotional offer",
        "discounts available with special deals",
        "exclusive offer",
        "offers for me",
        "my offers"
    ]

    offersType = [
        "Plan & Devices offers",
        "Data & voice offers",
        "data bundles special offers",
        "voice bundles special offers",
        "special offers for bundles"
    ]

    # Define the utterance templates
    utterances = [
        "manage bundles",
        "manage add ons",
        "i want add ons services",
        "{genQa} additional services {INTERROGATIVE_WORDS} I add to my plan",
        "Tell me about the add-on options available",
        "your add-on packages",
        "{INTERROGATIVE_WORDS} you explain the different add on services you offer",
        "the details of your adds on features",
        "{genQa} the add ons to purchase",
        "explore the addon services",
        "i want to enhance my current plan and add more bundles",
        "Check Bundles Status",
        "I am looking for {bundleType}",
        "{bundleType}",
        "{voiceType}",
        "i want to {buyBundle} bundles",
        "{buyBundle} {bundleType}",
        "{buyBundle} {voiceType}",
        "explain please the different bundle options",
        "I'd like to {buyBundle} {bundleType} to my existing bundle",
        "{genQa} bundles do you offer",
        "show me available {bundleType} bundles",
        "I need a {bundleType} for {voiceType}. {genQa} you offer",
        "{checkFix}",
        "{specialdeals}",
        "{how_phrases} get {specialdeals}?",
        "{specialdeals} of {offersType}",
        "I am looking for {specialdeals}",
        "any {specialdeals} for my number?",
        "{specialdeals} on my account?",
        "{how_phrases} access a {specialdeals}?",
        "My {offersType} for this month",
        "{PlanDevicesDeals}",
        "i want to {buy} {offersType}",
        "{genQa} the available {specialdeals} for {offersType} for me"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "bundleType": bundleType,
        "voiceType": voiceType,
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
        "checkFix": checkFix,
        "specialdeals": specialdeals,
        "offersType": offersType,
        # "buyBundle": buyBundle
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
    file_name = f'manage_bundles_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
