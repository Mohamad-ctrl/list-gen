import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    troubleshootingType = [
        "an issue with my billing",
        "trouble with billing",
        "billing problem",
        "mobile data is not working properly",
        "facing an issue with my mobile internet speed",
        "mobile data is extremely slow",
        "having trouble with my data plan",
        "internet is not working on my smartphone",
        "data plan seems to be having issues",
        "internet is not loading on my phone",
        "struggling with my mobile internet connection",
        "data service is not functioning",
        "data bundles issues",
        "diagnose my mobile net issue",
        "experiencing poor network coverage",
        "network signal is weak in my area",
        "not getting proper network coverage",
        "not receiving any network signal",
        "experiencing voice call issues",
        "voice bundle is not working",
        "issue with my voice package",
        "need help with my voice bundle subscription",
        "voice bundle problem",
        "difficulties with my voice bundle service",
        "challenges with my voice bundle usage",
        "unable to use my voice bundle",
        "trouble with the voice bundle",
        "voice bundle error",
        "trouble with international roaming",
        "not able to use roaming services abroad",
        "unable to use roaming services while traveling",
        "phone isn't working while I'm abroad",
        "issues with my roaming service",
        "troubleshoot my roaming service",
        "home Wi-Fi is not connecting",
        "home internet keeps disconnecting",
        "home internet is down",
        "troubleshoot my home Wi-Fi",
        "troubleshoot my home network",
        "smart home devices are not connecting to the network",
        "problem with my home Wi-Fi signal strength",
        "home network is running slow",
        "diagnose and fix my home network problems",
        "issue with home connection",
        "fixed line issues",
        "fixed services problem",
        "landline issues"
    ]

    troubleshooting = [
        "troubleshooting",
        "troubleshoot",
        "fix",
        "solve",
        "resolve",
        "fix my issue"
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

    PayChargeIssue = [
        "payment / recharge issue",
        "pay/recharge problem",
        "payment trouble",
        "payment failed",
        "payment hasn't gone through",
        "payment was not accepted",
        "online payment is not working",
        "double charge",
        "payment problem",
        "issue with my payment",
        "issue with doing payment",
        "not able to make payment",
        "problem with payment",
        "du recharge is not working",
        "du recharge not credited",
        "recharge trouble",
        "recharge failed",
        "recharge hasn't gone through",
        "recharge was not accepted",
        "online recharge is not working",
        "not able to recharge",
        "issue with recharge"
    ]

    # Define the utterance templates
    utterances = [
        "have a problem",
        "My internet is not working",
        "I can't make calls",
        "My calls keep dropping",
        "help me to fix my issues",
        "i have an issue with your services",
        "your services are not working properly",
        "i have {troubleshootingType} please help me",
        "i'm {troubleshootingType}",
        "{how_phrases} {troubleshooting} {troubleshootingType}",
        "{troubleshootingType}",
        "{genQa} {troubleshootingType}",
        "{INTERROGATIVE_WORDS} {troubleshooting} {troubleshootingType}",
        "{PayChargeIssue}",
        "{how_phrases} to {troubleshooting} my {PayChargeIssue}",
        "facing {PayChargeIssue}",
        "{genQa} {INTERROGATIVE_WORDS} the reason of {PayChargeIssue}",
        "my {PayChargeIssue} {genQa} {INTERROGATIVE_WORDS}",
        "i have {troubleshootingType} i am unable to {PayChargeIssue}",
        "help me i am {troubleshooting} with {troubleshootingType} services"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "troubleshootingType": troubleshootingType,
        "troubleshooting": troubleshooting,
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
        "PayChargeIssue": PayChargeIssue
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
    file_name = f'troubleshot_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
