import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the utterance templates
    utterances = [
        "hayyak",
        "hayyak services",
        "prepaid services",
        "recharge services",
        "recharge menu",
        "show me the recharge services",
        "top up services",
        "{damaged} Voucher",
        "My voucher card {INTERROGATIVE_WORDS} {damaged}",
        "The voucher code I received {damaged}",
        "I {INTERROGATIVE_WORDS} make out the numbers on my voucher due to {damaged}",
        "I bought a voucher but it seems to be {damaged}",
        "{genQa} to do if the voucher {damaged}",
        "help me with my {damaged} voucher",
        "{how_phrases} use the {damaged} voucher",
        "Unlock recharge card",
        "My recharge card is locked and I want to {unlockCard} it",
        "help me {unlockCard}",
        "{INTERROGATIVE_WORDS} {unlockCard}",
        "{genQa} the process to {unlockCard}",
        "I'm having trouble {unlockCard}",
        "{how_phrases} {unlockCard}",
        "I have a recharge card that I need to get {unlockCard}",
        "{topUp}",
        "i want to {topUp}",
        "{how_phrases} {topUp}",
        "{INTERROGATIVE_WORDS} I make {topUp} {topUpfor}",
        "{genQa} {INTERROGATIVE_WORDS} {topUp}",
        "ways to {topUp}",
        "Let me {topUp} please {topUpfor}",
        "I have to {topUpfor} {INTERROGATIVE_WORDS} help",
        "I'm ready to {topUp} now",
        "{topUp} {topUpfor}",
        "i need to {topUp} {how_phrases} do that",
        "{INTERROGATIVE_WORDS} you show me {checkHistory}",
        "{genQa} {checkHistory}",
        "{checkHistory}",
        "Display {checkHistory}",
        "i want to {check} {checkHistory} please",
        "{how_phrases} to {check} my {checkHistory}",
        "Let me know the {checkHistory}",
        "show me the list of {checkHistory}",
        "data",
        "{moreData}",
        "I need {moreData}",
        "i am running out of data and i want more {genQa}",
        "{INTERROGATIVE_WORDS} help me to purchase {moreData}",
        "{genQa} the {moreData} available options",
        "I want to explore options for {moreData}",
        "{how_phrases} to get {moreData}",
        "{dataConsumption}",
        "status of my {dataConsumption}",
        "{how_phrases} {dataConsumption}",
        "{genQa} {dataConsumption}",
        "{INTERROGATIVE_WORDS} help me to know {dataConsumption}",
        "Show me {dataConsumption} for this month",
        "{how_phrases} close am I to reaching {dataConsumption}",
        "the breakdown of {dataConsumption}",
        "{INTERROGATIVE_WORDS} provide details on {dataConsumption}",
        "plans",
        "Products & Plans",
        "{plans}",
        "show me {plans}",
        "{plansHelp} {plans}",
        "i want to check {plans} {plansHelp}",
        "explore the {plans}",
        "{genQa} the {plans} available",
        "{INTERROGATIVE_WORDS} provide the details of {plans}",
        "{how_phrases} to {subscribe} new {plans}",
        "change plan",
        "i want to change my plan",
        "{INTERROGATIVE_WORDS} i {changePlan}",
        "{how_phrases} to {changePlan}",
        "{genQa} i have to do to {changePlan}",
        "{changePlan}",
        "balance",
        "{balance}",
        "{how_phrases} to {check} my {balance}",
        "I want to know my {balance}",
        "{genQa} {balance}",
        "I'm not sure {how_phrases} {balance} I have left",
        "{genQa} {balance} expire",
        "{check} {balance}",
        "Give me an update on {balance}",
        "{INTERROGATIVE_WORDS} {check} {balance}",
        "{control}",
        "i want help with {control}",
        "{genQa} {INTERROGATIVE_WORDS} i do to {control}",
        "best way to {control} for {controlDataDevice}",
        "{control} options",
        "my mobile is {controlDataDevice} {how_phrases} {control}",
        "baqati",
        "baqati services",
        "{how_phrases} am I {commitment} my postpaid subscription",
        "{commitment}",
        "{genQa} the {commitment} for my current subscription",
        "{commitment} in baqati",
        "my baqati {commitment}",
        "{INTERROGATIVE_WORDS} i know {commitment} for my postpaid subs",
        "the details of my {commitment} please",
        "billing",
        "{billing}",
        "i want to {billing}",
        "{INTERROGATIVE_WORDS} i {billing}",
        "{genQa} {billing}",
        "{how_phrases} {INTERROGATIVE_WORDS} {billing}",
        "Let me {billing}",
        "Baqati Gift",
        "show me my Baqati Gifts",
        "{genQa} baqati gifts i have",
        "provide with the list of baqati gifts",
        "{INTERROGATIVE_WORDS} more about baqati gifts",
        "{how_phrases} get baqati gift",
        "i have any baqati gift",
        "{ComplaintStatus}",
        "{check} {ComplaintStatus}",
        "{how_phrases} {INTERROGATIVE_WORDS} I {check} my {ComplaintStatus}",
        "help me to {check} my {ComplaintStatus}",
        "i am asking about my {ComplaintStatus}",
        "i want to {check} my {ComplaintStatus}",
        "i'd like to ask about my {ComplaintStatus} {genQa} {INTERROGATIVE_WORDS} the update?",
        "{INTERROGATIVE_WORDS} give me an update on my {ComplaintStatus}",
        "{how_phrases} my {ComplaintStatus} progressing",
        "add ons services",
        "{addOns}",
        "i want to know {addOns}",
        "{INTERROGATIVE_WORDS} show me {addOns}",
        "{how_phrases} to know the {addOns}",
        "{genQa} {addOns}",
        "eshop",
        "{eshop}",
        "i want to check {eshop}",
        "{INTERROGATIVE_WORDS} check the {eshop} for {devices}",
        "{INTERROGATIVE_WORDS} {devices} {eshop} in omantel",
        "{genQa} the {eshop}",
        "{how_phrases} know if {eshop}",
        "{devices} {eshop}",
        "{Orderstatus}",
        "i want to {check} {Orderstatus}",
        "{how_phrases} {INTERROGATIVE_WORDS} I {check} {Orderstatus}?",
        "i am asking about my {Orderstatus}",
        "{genQa} {INTERROGATIVE_WORDS} {Orderstatus}?",
        "{INTERROGATIVE_WORDS} {Orderstatus} prepared or not yet",
        "i am asking if there {INTERROGATIVE_WORDS} any update related to {Orderstatus}",
        "{INTERROGATIVE_WORDS} my {Orderstatus} being still pending?",
        "i didn't receive {Orderstatus} yet {genQa}",
        "i have an order and i want to {check} the status",
        "{checkstatus} {Orderstatus}",
        "Makasib",
        "tell me more about makasib",
        "{genQa} makasib",
        "i want to {makasib}",
        "{INTERROGATIVE_WORDS} {makasib}",
        "{genQa} the steps to {makasib}",
        "{how_phrases} {INTERROGATIVE_WORDS} {makasib}",
        "i heard about makasib recently {how_phrases} to {makasib}",
        "join omantel family",
        "i want to be omantel user",
        "{how_phrases} become user in omantel",
        "{how_phrases} {joinOmantel}",
        "i want to {joinOmantel}",
        "{genQa} the steps to {joinOmantel}",
        "{INTERROGATIVE_WORDS} {joinOmantel}",
        "SIM services",
        "i want to {buySIM}",
        "i need to {replacement}",
        "{replacement}",
        "{buySIM}",
        "{replacement} for {esimType}",
        "i have {esimType} and i want to {replacement}",
        "{genQa} if i {replacement}",
        "{INTERROGATIVE_WORDS} help me to {buySIM}",
        "update profile",
        "{updateProfile}",
        "i want to {updateProfile}",
        "{INTERROGATIVE_WORDS} {updateProfile}",
        "{how_phrases} {INTERROGATIVE_WORDS} {updateProfile}",
        "{genQa} do to {updateProfile}",
        "VAT",
        "{VAT}",
        "{genQa} the {VAT}",
        "tell me about {VAT}",
        "{how_phrases} to know {genQa} the {VAT}",
        "{INTERROGATIVE_WORDS} provide details on vat or tax",
        "nearest Outlets",
        "i want to know the outlest nearby",
        "list of omantel outlets",
        "{genQa} the nearest Outlet"
    ]

    damaged = [
        "got scratched",
        "has some damage",
        "voucher code is unreadable",
        "got crumpled",
        "torn",
        "destroyed",
        "smashed",
        "scratched and unreadable",
        "illegible",
        "defective"
    ]

    unlockCard = [
        "Unlock recharge card",
        "Activate my locked card",
        "Unlock my prepaid card",
        "Enable my recharge card",
        "Unlock"
    ]

    topUp = [
        "recharge here",
        "top up now",
        "refill my prepaid mobile plan here",
        "I'm running low on my prepaid balance",
        "my prepaid plan is about to expire",
        "top up from others",
        "ask someone to top up my account for me",
        "get a top-up from my friend",
        "recharge request",
        "top up request",
        "someone else top up",
        "get a top-up from a family member",
        "receive a top-up from someone else",
        "get a top-up from my spouse to mine",
        "receive a top-up credit from someone else"
    ]

    checkHistory = [
        "Topup History",
        "Recharge history",
        "Recent top-up transactions",
        "Last few recharge details",
        "Top-up records",
        "Recharge transaction log",
        "My top-up activity",
        "List of my recent recharge purchases",
        "The top-up amounts I made recently",
        "Last recharge",
        "Recharge statement",
        "History of my prepaid account recharges",
        "Money Transfer History",
        "Recent money transfers",
        "Money transfer records",
        "History of my money transfers",
        "List of my past money transfers",
        "Money transfer activity",
        "List of money transfers I have made",
        "Past money transfers",
        "Call history",
        "Recent call logs",
        "Call records",
        "The calls I've made recently",
        "My call activity",
        "Summary of my call history",
        "Paid Bills History",
        "Previous bill payments",
        "Details of my paid bills",
        "Review the bills I've already paid",
        "Bills I've settled recently",
        "Payment history",
        "Payment records",
        "Payment transactions",
        "Summary of my payment activity",
        "Payments I've made"
    ]

    moreData = [
        "more data",
        "additional data",
        "extra data",
        "new data bundles",
        "extra data bundles"
    ]

    dataConsumption = [
        "my data consumption",
        "data usage",
        "data have I used",
        "data I consumed",
        "remaining data",
        "my data limit"
    ]

    plans = [
        "Postpaid Baqati Plan",
        "Baqati plans",
        "Prepaid Hayyak Plan",
        "Hayyak plans",
        "Home Baiti Plan",
        "HBB plans"
    ]

    changePlan = [
        "Upgrade Hayyak plan",
        "Upgrade my prepaid plan",
        "Upgrade my current Hayyak plan",
        "Change prepaid plan",
        "Change my Hayyak plan",
        "Upgrade to Postpaid",
        "Upgrade from prepaid to Postpaid",
        "Upgrade to Baqati",
        "Upgrade from Hayyak to Baqati",
        "Move to Baqati",
        "Migrate from prepaid to Postpaid",
        "Plan migration from Hayyak to Baqati",
        "Switch from prepaid to Postpaid",
        "Change Baqati plan",
        "Upgrade my Baqati plan",
        "Upgrade my Postpaid plan",
        "Upgrade my current Baqati plan"
    ]

    balance = [
        "show me my balance",
        "remaining balance",
        "prepaid balance amount",
        "check mobile balance",
        "see account balance",
        "remaining credit",
        "my current balance",
        "my balance status",
        "my available balance"
    ]

    control = [
        "Control Credit",
        "Manage my credit",
        "Controlling my credit usage",
        "Credit control",
        "Better manage my credit",
        "Credit management",
        "Control Data",
        "Manage my data",
        "Data control",
        "Controlling data",
        "Monitor my data",
        "Data management"
    ]

    commitment = [
        "My Commitment",
        "Commitment period",
        "Contract duration",
        "Committed to",
        "Duration of my commitment"
    ]

    billing = [
        "View bills",
        "Bill Details",
        "My bills",
        "Unpaid bill",
        "Bill Breakdown",
        "The breakdown of my bills",
        "Pay Bill",
        "Pay my bills",
        "Settle my account balance",
        "Make a payment for my outstanding charges",
        "Pay my outstanding bills",
        "Pay my monthly invoice",
        "Pay my outstanding balance",
        "Clear my account balance"
    ]

    ComplaintStatus = [
        "Complaint Status",
        "Complaint details",
        "Status of my complaint",
        "Complaint situation",
        "Ticket status",
        "The status of my ticket",
        "Open ticket",
        "Complaint request",
        "Raised complaint status",
        "The issue I reported earlier",
        "Open case",
        "The ticket I opened",
        "Open service case",
        "The complaint I filed"
    ]

    addOns = [
        "Active VAS Subs.",
        "My active value-added services subscriptions",
        "VAS services I'm currently subscribed to",
        "Value-added services I'm paying for",
        "VAS subscriptions do I have enabled on my plan",
        "VAS subscription details",
        "VAS list",
        "Value-added services",
        "List of VAS",
        "All VAS services",
        "Gift Cards"
    ]

    eshop = [
        "Device Available?",
        "Check device availability",
        "This device is available",
        "Out of stock",
        "Available in stock",
        "Available in Omantel",
        "Eligible for installment",
        "The possibility of buying a device through Omantel",
        "Installment eligibility",
        "Getting installment for device in Omantel",
        "Installment plan",
        "Eligible to pay in installments",
        "Pay in installments eligibility",
        "Am I eligible to get installment and buy a device",
        "Am I eligible to pay in installments"
    ]

    Orderstatus = [
        "Product request status",
        "The status of my order",
        "Product status",
        "Order tracking",
        "Track order",
        "Order status",
        "Ordered device",
        "Product ordered"
    ]

    makasib = [
        "Register to Makasib",
        "Join Makasib",
        "Sign up for Makasib",
        "Subscribe to Makasib",
        "Add my account to Makasib",
        "Reset Makasib Password",
        "Change my Makasib password",
        "Reset Makasib PW",
        "I forgot my Makasib password",
        "Update the password of Makasib"
    ]

    joinOmantel = [
        "Transfer to Omantel",
        "Switch my number to Omantel",
        "Migrate to Omantel",
        "Switching to Omantel",
        "Shift my number to Omantel",
        "Convert my number to Omantel",
        "Buy new Home Internet",
        "Get new home internet",
        "New home internet request",
        "Apply for home internet request",
        "Apply for HBB"
    ]

    buySIM = [
        "Buy New Prepaid SIM",
        "Buy new Hayyak SIM",
        "Get new Hayyak SIM",
        "Apply for new Hayyak SIM",
        "Buy New Postpaid SIM",
        "Buy new Baqati SIM",
        "Get new Baqati SIM",
        "Apply for new Baqati SIM"
    ]

    updateProfile = [
        "Update bill language",
        "Change bill language",
        "Change the language of my bills",
        "Reset bill language",
        "Update contact No.",
        "Update my contact number",
        "Update my mobile number",
        "Change my contact number",
        "Update my phone number in your records",
        "Update email address",
        "Change my email address",
        "Change Primary Number",
        "Update my primary number"
    ]

    vAT = [
        "VAT on New SIMs",
        "New SIM VAT",
        "VAT for Prepaid Users",
        "Hayyak VAT",
        "VAT for Postpaid Users",
        "Baqati VAT",
        "VAT on Home Internet",
        "Baiti VAT",
        "VAT on Devices",
        "Devices VAT",
        "VAT for Business Owners"
    ]

    topUpfor = [
        "Recharge for me",
        "Top up for me",
        "For myself",
        "To me",
        "For someone else",
        "For my friend",
        "For family",
        "For wife",
        "For husband",
        "For son",
        "For daughter"
    ]

    plansHelp = [
        "Show me all plans",
        "All plans of",
        "Display all plans",
        "Find me the best plan",
        "Help me find the best plan",
        "Find the best plan for me",
        "Recommend the best plan for me"
    ]

    check = [
        "check",
        "find",
        "inquire",
        "track",
        "calculate",
        "see",
        "view"
    ]

    controlDataDevice = [
        "Apple",
        "IOS devices",
        "Android"
    ]

    devices = [
        "Apple",
        "samsung",
        "Huawei",
        "lenovo",
        "oppo"
    ]

    replacement = [
        "Replace lost/damaged SIM",
        "My SIM got damaged; I need a new one",
        "Lost SIM replacement",
        "Misplaced my SIM card and I want to replace it",
        "SIM replacement",
        "Replace my SIM",
        "eSIM",
        "Get eSIM instead of my current SIM",
        "Switch from a physical SIM to an eSIM",
        "Get an eSIM instead of a regular SIM card",
        "Change from a SIM to an eSIM",
        "Converting my SIM to an eSIM",
        "Swap out my SIM for an eSIM",
        "Replace PKI",
        "PKI replacement",
        "Transfer PKI to my SIM"
    ]

    subscribe = [
        "subscribe",
        "apply for",
        "set",
        "get",
        "buy"
    ]

    esimType = [
        "Apple",
        "Android",
        "Huawei"
    ]

    iNTERROGATIVE_WORDS = [
        "Can",
        "Can i do",
        "Could",
        "Should",
        "Should i do",
        "Would",
        "Is",
        "Are",
        "was",
        "were",
        "Will",
        "Did",
        "Do",
        "Do not",
        "Does",
        "May",
        "can be",
        "could be",
        "may be",
        "will be",
        "should be",
        "Do i need to be",
        "do i have to be",
        "do i do",
        "Is being",
        "must i be",
        "shall",
        "shall i",
        "can't",
        "cannot",
        "can not"
    ]

    how_phrases = [
        "how",
        "how does",
        "how to",
        "how can i",
        "how do i",
        "how i",
        "how could i",
        "how can i",
        "how can",
        "how could",
        "how will",
        "how many",
        "how much",
        "how long"
    ]

    genQa = [
        "What",
        "When",
        "Where",
        "Who",
        "Which",
        "Whom",
        "Whose",
        "Why",
        "what's",
        "what is",
        "what are"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_lists = {
        "damaged": damaged, 
        "unlockCard": unlockCard,
        "topUp": topUp,
        "checkHistory": checkHistory,
        "moreData": moreData,
        "dataConsumption": dataConsumption,
        "plans": plans,
        "changePlan": changePlan,
        "balance": balance,
        "control": control,
        "commitment": commitment,
        "billing": billing,
        "ComplaintStatus": ComplaintStatus,
        "addOns": addOns,
        "eshop": eshop,
        "Orderstatus": Orderstatus,
        "makasib": makasib,
        "joinOmantel": joinOmantel,
        "buySIM": buySIM,
        "updateProfile": updateProfile,
        "VAT": vAT,
        "topUpfor": topUpfor,
        "plansHelp": plansHelp,
        "check": check,
        "controlDataDevice": controlDataDevice,
        "devices": devices,
        "replacement": replacement,
        "subscribe": subscribe,
        "esimType": esimType,
        "INTERROGATIVE_WORDS": iNTERROGATIVE_WORDS,
        "how_phrases": how_phrases,
        "genQa": genQa

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
    file_name = f'omantel_1{formatted_date_time}.xlsx'
    df.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations)} questions and saved to {file_name}")