import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided

    Orderstatus = [
        "product request status",
        "pending sales orders",
        "the status of my sales order",
        "Sales Order status",
        "product status",
        "sales order tracking",
        "sales order status summary",
        "sales order situation",
        "the situation of my request related to sales order",
        "my last sales order",
        "my online sales order"
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

    checkstatus = [
        "check",
        "find",
        "inquire",
        "inquiry",
        "track",
        "know",
        "look at",
        "double check",
        "held in check",
        "review",
        "assure",
        "ensure",
        "check off",
        "look on",
        "trail",
        "trace",
        "tracking on",
        "tracery",
        "show me"
    ]

    trackway = [
        "Order ID",
        "order number",
        "order no.",
        "Mobile number",
        "phone number",
    ]


    ComplaintStatus = [
        "trouble tickets",
        "Complaint Status",
        "Complaint details",
        "the state of my complaint",
        "status of my complaint",
        "complaint situation",
        "status quo of my Complaint",
        "update related to my last complain",
        "update related to my all Complains",
        "the situation of my complaint",
        "ticket status",
        "the status of my ticket",
        "ticket",
        "complain",
        "open ticket",
        "complaint request",
        "raised complaint status",
        "service complaint",
        "the issue I reported earlier",
        "open case",
        "the ticket I opened",
        "open service case",
        "the complaint I filed"
    ]


    # Define the utterance templates
    utterances = [
        "{Orderstatus}",
        "i want to {checkstatus} {Orderstatus}?",
        "{how_phrases} {INTERROGATIVE_WORDS}  I {checkstatus} {Orderstatus}?",
        "i am asking about my {Orderstatus}",
        "{genQa} {INTERROGATIVE_WORDS} {Orderstatus}?",
        "{Orderstatus} {genQa} {INTERROGATIVE_WORDS} packed , collected and delivering ?",
        "{INTERROGATIVE_WORDS} {Orderstatus} prepaird or not yet?",
        "i {INTERROGATIVE_WORDS} like to {checkstatus} about {Orderstatus}",
        "{how_phrases} {checkstatus} my request for {Orderstatus}?",
        "{checkstatus} my {Orderstatus} please",
        "i am {checkstatus} if there {INTERROGATIVE_WORDS} any update related to {Orderstatus}",
        "{INTERROGATIVE_WORDS} my {Orderstatus} being still pending ?",
        "i didnt receive {Orderstatus} yet {genQa}",
        "{INTERROGATIVE_WORDS} {checkstatus} the status of my order",
        "i have an order and i want to {checkstatus} the status",
        "{checkstatus} {Orderstatus} by {trackWay}",
        "{ComplaintStatus}",
        "{checkstatus} {ComplaintStatus}",
        "{how_phrases} {INTERROGATIVE_WORDS} I {checkstatus} my {ComplaintStatus} on the du app?",
        "help me to {checkstatus} my {ComplaintStatus}",
        "i am asking about my {ComplaintStatus}",
        "i want to {checkstatus} my {ComplaintStatus}",
        "i am {checkstatus} if there {INTERROGATIVE_WORDS} any {ComplaintStatus}",
        "i'd like to ask about my {ComplaintStatus} {genQa} {INTERROGATIVE_WORDS} the update?",
        "{INTERROGATIVE_WORDS} give me an update on my {ComplaintStatus}",
        "{how_phrases} my {ComplaintStatus} progressing"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "Orderstatus": Orderstatus, 
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
        "checkstatus": checkstatus,
        "trackWay": trackway,
        "ComplaintStatus": ComplaintStatus
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
    file_name = f'order_complaint_status_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
