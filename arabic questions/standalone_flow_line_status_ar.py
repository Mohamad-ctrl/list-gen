import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided

    how_phrasesAR = ["كيف يمكنني", "كيف", "ممكن أعرف كيف", "شلون", "كيفية"]

    wantAr = ["أبغى", "أبي", "أريد", "أبا", "بدي", "ريد", "ودي", "أود", "أحتاج"]

    INTERROGATIVE_WORDSar = [
        "هل يمكنني", "هل يمكنك", "هل", "ما هي", "ما هو", "وش", "وش هي", "إيش", "ما هو", 
        "شنو", "شو هو", "شو هي", "شو", "قديش", "كم", "ماذا", "لماذا", "ليش"
    ]

    standalonear = [
        "حالة خطي",
        "حالة عقدي",
        "حالة خطتي",
        "اسم اشتراكي",
        "فوائد باقتي",
        "مزايا خطي الحالي",
        "رسوم المكالمات الدولية على خطي",
        "تاريخ عقدي",
        "تفاصيل اشتراكي",
        "تفاصيل عقدي",
        "تاريخ تفعيل العقد",
        "حالة الحساب"
    ]

    # Define the utterance templates
    utterancesAR = [
        "{wantAr} أعرف {standalonear}",
        "الاستعلام عن {standalonear}",
        "{INTERROGATIVE_WORDSar} {standalonear}",
        "{standalonear}",
        "{standalonear}  من فضلك",
        "{how_phrasesAR} {standalonear} الخاص بي"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "standalonear": standalonear
    }

    # Generate all combinations and remove duplicates using a set
    all_combinations_ar = set()

    for utterance in utterancesAR:
        placeholders = [f"{{{key}}}" for key in placeholder_listsAR if f"{{{key}}}" in utterance]
        if placeholders:
            combos = itertools.product(*(placeholder_listsAR[key.strip("{}")] for key in placeholders))
            for combo in combos:
                question = utterance
                for placeholder, value in zip(placeholders, combo):
                    question = question.replace(placeholder, value)
                all_combinations_ar.add(question)
        else:
            all_combinations_ar.add(utterance)

    # Save to Excel
    df_ar = pd.DataFrame(list(all_combinations_ar), columns=["Questions"])
    currentDate = datetime.now()

    # Format the date and time
    formatted_date_time = currentDate.strftime("%d-%m_%I.%M%p").lower()

    # Create the file name
    file_name = f'standalone_ar_{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
