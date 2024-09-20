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

    # Define the utterance templates
    utterancesAR = [
        "القائمة الرئيسية",
        "قائمة الخدمات",
        "الخدمات",
        "العودة إلى القائمة الرئيسية",
        "أرني القائمة الرئيسية من فضلك",
        "{how_phrasesAR} الرجوع إلى القائمة الرئيسية",
        "{wantAr} القائمة الرئيسية",
        "رقم ثاني",
        "رقم هاتف آخر",
        "{wantAr} إدخال رقم هاتف آخر",
        "{how_phrasesAR} إدخال رقم هاتف مختلف",
        "{wantAr} أدخل رقم ثاني",
        "إنهاء الدردشة",
        "إيقاف الدردشة",
        "إيقاف",
        "أنهي المحادثة",
        "إرسال رمز تحقق آخر",
        "إعادة إرسال رمز تحقق جديد",
        "رمز التحقق منتهي الصلاحية, {wantAr} رمز تحقق جديد",
        "أعد إرسال رمز التحقق من فضلك",
        "أرسل لي رمز تحقق جديد",
        "لا",
        "لا شيء",
        "شكراً",
        "باي",
        "لا شكراً",
        "لا ما {wantAr} شيء شكراً",
        "ليس لدي سؤال آخر",
        "ماعندي أسئلة ثانية",
        "ما {wantAr} شيء ثاني شكراً",
        "نعم",
        "ايوا",
        "نعم لدي سؤال آخر",
        "اي عندي سؤال ثاني",
        "{wantAr} أسأل عن شي ثاني",
        "{wantAr} مساعدة في موضوع آخر",
        "سؤال ثاني"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
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
    file_name = f'general_ar_{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
