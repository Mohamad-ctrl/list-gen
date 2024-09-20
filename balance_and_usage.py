import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    balance = [
        "free units", "balance", "required balance", "remaining free units balance",
        "remaining balance in Credit Wallet", "prepaid balance", "mobile balance",
        "remaining balance", "account balance", "remaining credit", "du balance",
        "postpaid balance", "Credit balance", "my current balance and free units",
        "units", "my balance status", "account balance and available units",
        "data remaining", "du data balance", "data balance", "remaining data",
        "voice remaining", "voice minutes balance", "voice minutes remaining",
        "calling bundle balance"
    ]

    check = ["check", "find", "find out", "inquire", "inquiry", "track", "inquiries", "calculate"]

    PayChargeNow = [
        "pay my bill", "pay a postpaid bill now", "pay online now", "du bill online", "quick pay", 
        "online payment", "pay du monthly bills now", "pay my pending invoices", "clear pending invoices", 
        "payment for my phone plan", "pay for my postpaid service", "settle my mobile phone bill", 
        "pay my bill", "my postpaid plan payment is overdue", "pay my du postpaid bill now", 
        "pay for yourself", "pay for myself", "pay for my friend", "gotta pay my phone bill", 
        "top up my postpaid plan", "settle my outstanding balance", "pay my telecom charges", 
        "clear my postpaid dues", "confirm the amount I need to pay for my postpaid plan", 
        "proceed payment now", "Pay for you/friend",
        "top up my prepaid plan", "refill my prepaid mobile plan", "add credit to my prepaid account", 
        "recharge my phone plan", "refill my prepaid minutes", "process of recharging my plan", 
        "purchase a top-up for my prepaid service", "I'm running low on my prepaid balance", 
        "I want to add more now", "my prepaid plan is about to expire", "I need to recharge it", 
        "reload my prepaid account", "recharging my phone credit", "recharging my prepaid number online", 
        "recharge for myself", "recharge for a friend", "recharge for you/friend"
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

    PayChargeHistory = [
        "billing history", "detailed bill", "bill summary", "bill statement", "last payment",
        "my recent bill payments", "my payment records", "details of my last payment",
        "payment details for my home internet service", "recent bill payments for my postpaid plan",
        "list of all my bill payments made", "summary of postpaid bill payments for the previous quarter", "recent payment transactions for my account",
        "my past transactions", "what I have paid for recently", "track my payment history", "last recharge",
        "recharge statement", "recent recharge transactions", "my prepaid recharge history", "details of my last recharge",
        "prepaid recharge records", "history of my prepaid account recharges", "list of previous recharges", "my recent phone refills"
    ]
    usageBreakdown = [
        "usage breakdown",
        "usage details",
        "bundle usages breakdown",
        "View usage breakdown",
        "my usage information",
        "the breakdown of my plan usage",
        "summary of my usage",
        "the usage statistics",
        "usage summary",
        "Bill Details"
    ]

    TopUsageReasons = [
        "Top Usage Reasons",
        "recurring charges increased",
        "usage charges increased",
        "high data usage reason",
        "my usage has been high lately",
        "usage much higher than usual"
    ]

    # Define the utterance templates
    utterances = [
        "{balance}",
        "{how_phrases} to {check} my {balance}",
        "{how_phrases} {check} what my {balance} {INTERROGATIVE_WORDS}?",
        "inquiring about {balance}",
        "I want to know my {balance}",
        "{how_phrases} {balance} {INTERROGATIVE_WORDS} i have left",
        "i am not able to find my {balance} can you help me",
        "{genQa} {balance}",
        "I'm not sure {how_phrases} {balance} I have left",
        "{INTERROGATIVE_WORDS} {balance} low or high",
        "{how_phrases} {INTERROGATIVE_WORDS} {balance} last",
        "{genQa} {balance} expire",
        "{check} {balance}",
        "Give me an update on {balance}",
        "{how_phrases} am I doing on {balance}",
        "i want to {check} the status of my {balance}",
        "{PayChargeNow}",
        "i want to {PayChargeNow}",
        "{how_phrases} {PayChargeNow}",
        "{INTERROGATIVE_WORDS} I make {PayChargeNow}",
        "{genQa} {INTERROGATIVE_WORDS} {PayChargeNow}",
        "ways to {PayChargeNow}",
        "Let me {PayChargeNow} please",
        "I have to {PayChargeNow} {INTERROGATIVE_WORDS} help",
        "{INTERROGATIVE_WORDS} guide me through {PayChargeNow} process",
        "I'm ready to {PayChargeNow} now",
        "please confirm the {PayChargeNow}",
        "i have {PayChargeNow} i want to do now",
        "{INTERROGATIVE_WORDS} you show me {PayChargeHistory}",
        "i need to view my {PayChargeHistory}",
        "{genQa} {PayChargeHistory}",
        "{PayChargeHistory}",
        "Display {PayChargeHistory}",
        "i want to see a {PayChargeHistory} please",
        "{how_phrases} to check my {PayChargeHistory}",
        "{usageBreakdown}",
        "{INTERROGATIVE_WORDS} show me my {usageBreakdown}",
        "i want to know my {usageBreakdown}",
        "{how_phrases} to understand my {usageBreakdown}",
        "I'd like to see {usageBreakdown} please",
        "show me my {usageBreakdown}",
        "{genQa} my {usageBreakdown}",
        "{genQa} have my monthly {TopUsageReasons}",
        "{INTERROGATIVE_WORDS} i know {genQa} have my {TopUsageReasons}",
        "{genQa} i have {TopUsageReasons} in this month for data and minutes",
        "i want to {check} about {TopUsageReasons}",
        "{genQa} {INTERROGATIVE_WORDS} the reason of {TopUsageReasons} this month",
        "I've noticed {TopUsageReasons} {INTERROGATIVE_WORDS} you explain",
        "My {TopUsageReasons}. {genQa} {INTERROGATIVE_WORDS} causing excessive usage"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "balance": balance,
        "check": check,
        "PayChargeNow": PayChargeNow,
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
        "PayChargeHistory": PayChargeHistory,
        "usageBreakdown": usageBreakdown,
        "TopUsageReasons": TopUsageReasons
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
    file_name = f'balance&usage_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"balance&usage generated {len(all_combinations)} questions")
