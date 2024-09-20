import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided
    hometype = [
        "Wireless",
        "Home Wireless 4G",
        "Home Wireless 5G",
        "5G home internet",
        "4G home internet",
        "unlimited 5G home wireless",
        "Fibe",
        "fiber internet",
        "FTTH",
        "FTTH NETWORK"
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

    newProduct = [
        "fixed",
        "fixed line",
        "prepaid",
        "postpaid",
        "Enterprise Mobile",
        "business mobile",
        "mobile plans for Enterprise",
        "mobile plans for business",
        "mobile plans for companies",
        "prepaid plans for companies",
        "postpaid plans for companies",
        "Enterprise prepaid",
        "Enterprise postpaid",
        "Enterprise Fixed",
        "Enterprise Internet & Connectivity",
        "internet for Enterprise",
        "business fixed",
        "fixed services for business",
        "internet services for business",
        "business lines",
        "Devices"
    ]

    subscribe = [
        "subscribe",
        "subscribe to",
        "subscribed",
        "apply",
        "subscription",
        "sign up",
        "set",
        "get",
        "purchase",
        "set up",
        "buy"
    ]

    devicesType = [
        "Phones",
        "mobiles",
        "mobile devices",
        "Tablets",
        "Ipad",
        "Watches",
        "smart watches",
        "apple watches",
        "samsung watches",
        "Gaming",
        "playstation",
        "Accessories",
        "mobile Accessories",
        "airpods",
        "headphones",
        "airtag",
        "charger",
        "cable"
    ]

    cost = ["cost", "fee", "fees", "payment", "charges"]

    phonesType = [
        "Apple",
        "iphone",
        "iphone 15",
        "iphone 15 pro max",
        "Samsung",
        "galaxy",
        "galaxy S24 ultra",
        "galaxy Z",
        "All phones",
        "all mobile devices",
        "oppo",
        "xiaom"
    ]

    # Define the utterance templates
    utterances = [
        "{newProduct} plans",
        "{hometype}",
        "{how_phrases} {INTERROGATIVE_WORDS} I {subscribe} a du {newProduct} plans?",
        "I am looking for du {newProduct} plans",
        "{newProduct} plan packages",
        "I want to know the {cost} for the du {newProduct} plan packages",
        "{hometype} connection",
        "i want to ask about {newProduct} {hometype} plans",
        "{how_phrases} {INTERROGATIVE_WORDS} I {subscribe} a {hometype}?",
        "I want {newProduct} plans",
        "I {INTERROGATIVE_WORDS} like to {subscribe} more details about {newProduct}",
        "help me with {newProduct} plans",
        "{genQa} {INTERROGATIVE_WORDS} the new du {newProduct} packages?",
        "{genQa} routers are included in du {newProduct} packages?",
        "{how_phrases} check my du {newProduct} plans?",
        "{how_phrases} {INTERROGATIVE_WORDS} I check network's speed at {newProduct}?",
        "{how_phrases} {subscribe} my broadband network?",
        "recommended {newProduct} plans",
        "{newProduct}",
        "explore our products",
        "explore the {newProduct}",
        "I've been hearing about some good {newProduct} deals by du",
        "{INTERROGATIVE_WORDS} offer me a good {newProduct} deal",
        "{genQa} your latest promotions on {newProduct}",
        "{INTERROGATIVE_WORDS} you have any special deals for new customers",
        "{INTERROGATIVE_WORDS} you tell me about the newest {newProduct} you offer",
        "I'm interested in {newProduct}. {genQa} your current options?",
        "I'm looking for the best value for money. {INTERROGATIVE_WORDS} you recommend a {newProduct} plan that suits my needs{devicesType}",
        "{phonesType}",
        "{genQa} available {devicesType}",
        "show me please the latest {phonesType}"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "hometype": hometype,
        "subscribe": subscribe,
        "INTERROGATIVE_WORDS": INTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa,
        "newProduct": newProduct,
        "cost": cost,
        "devicesType": devicesType,
        "phonesType": phonesType
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
    file_name = f'explour_products_{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")
